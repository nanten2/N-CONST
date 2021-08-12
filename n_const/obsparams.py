#!/usr/bin/env python3

__all__ = ["obsfile_parser"]

import re
import os
import copy
import importlib
from typing import Dict, Any
from dataclasses import dataclass

from tomlkit.toml_file import TOMLFile
from astropy.units.quantity import Quantity
from astropy.coordinates import Angle


def obsfile_parser(path: os.PathLike) -> Dict[str, Any]:
    """Observation parameters from alpaca style .obs file.

    Parameters
    ----------
    path: str

    Examples
    --------
    >>> obsfile_parser('test/horizon.obs')  # doctest: +NORMALIZE_WHITESPACE
    {'offset_Az': 0, 'offset_El': 0, 'lambda_on': 83.80613,\
    'beta_on': -5.37432, 'lambda_off': 82.559, 'beta_off': -5.6683,\
    'coordsys': 'HORIZONTAL', 'target': 'OriKL', 'vlsr': 0.0,\
    'tuning_vlsr': 0.0, 'cosydel': 'HORIZONTAL', 'otadel': 'N',\
    'start_pos_x': -120.0, 'start_pos_y': -120.0, 'scan_direction': 0,\
    'exposure': 0.6, 'otfvel': 50.0, 'otflen': 5.3999999999999995,\
    'grid': 30, 'N': 9, 'lamdel_off': 0, 'betdel_off': 0,\
    'otadel_off': 'N', 'nTest': 1, 'datanum': 9.0, 'lamp_pixels': 4,\
    'exposure_off': 10.0, 'observer': 'amigos', 'obsmode': 'LINEOTF',\
    'purpose': 2, 'tsys': 0, 'acc': 10, 'load_interval': 5,\
    'cold_flag': 'N', 'pllref_if': 1, 'multiple': 12, 'pllharmonic': 1,\
    'pllsideband': -1, 'pllreffreq': 0, 'restfreq_1': 230538.0,\
    'obsfreq_1': 230538.0, 'molecule_1': '12CO', 'transiti_1': 'J=2-1',\
    'lo1st_sb_1': 'U', 'if1st_freq_1': 4438.0, 'lo2nd_sb_1': 'L',\
    'lo3rd_sb_1': 'L', 'lo3rd_freq_1': 4100.0, 'if3rd_freq_1': 500.0,\
    'start_ch_1': 0, 'end_ch_1': 16383, 'restfreq_2': 220398.684,\
    'obsfreq_2': 220398.684, 'molecule_2': '13CO',\
    'transiti_2': 'J=2-1', 'lo1st_sb_2': 'L', 'if1st_freq_2': 5701.3,\
    'lo2nd_sb_2': 'L', 'lo3rd_sb_2': 'L', 'lo3rd_freq_2': 4100.0,\
    'if3rd_freq_2': 500.0, 'start_ch_2': 0, 'end_ch_2': 16383,\
    'fpga_integtime': 100, 'script': '200GHz/line_otf_car_rsky.alp'}
    """
    with open(os.path.abspath(path)) as f:
        content = f.read()
    content = re.sub(r"[\t ]*?#.*?\n", r"\n", content)
    content = re.sub(
        r"(\n.*?);(.*?)\n", r'\1="\2"\n', content
    )  # convert exec script to string of uniform format
    # get filename
    file_name = os.path.basename(path).split(".")[0]
    # build and execute the module
    spec = importlib.util.spec_from_loader(file_name, loader=None)
    pymodule = importlib.util.module_from_spec(spec)
    exec(content, pymodule.__dict__)
    ret = {k: v for k, v in pymodule.__dict__.items() if not k.startswith("__")}
    return ret


@dataclass(frozen=True)
class ObsParams:
    """Parse observation parameters."""

    def __post_init__(self):
        """Make Quantity.
        Parameters given as toml-array are converted into ``Quantity`` objects.
        """
        self._make_quantity()

    @classmethod
    def from_file(cls, path: os.PathLike):
        """Parse toml file.

        Parameters
        ----------
        path: str

        Notes
        -----
        All parameters declared in the toml file will be parsed. Table
        name of the toml file will be ignored.
        """
        inst = cls()
        params = TOMLFile(path).read()
        for param_group in params.values():
            for param_name, param in param_group.items():
                object.__setattr__(inst, param_name, param)
        inst._make_quantity()
        return inst

    def _make_quantity(self):
        params_dict = copy.deepcopy(self.__dict__)
        for name, value in params_dict.items():
            if not value:
                pass
            elif name.isupper():
                self.__dict__[name] = value
            elif name.islower():
                self.__dict__[name] = Quantity(value)
            else:
                self.__dict__[name] = Angle(value)

    def __getitem__(self, item):
        """Enable dot notation."""
        return getattr(self, item)

    def __repr__(self):
        return f"ObsParams({repr(self.__dict__)})"

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()


if __name__ == "__main__":
    pass
