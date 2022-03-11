__all__ = ["obsfile_parser", "ObsParams"]

import importlib
import os
import re
from pathlib import Path
from typing import Dict, Any

from astropy.coordinates import Angle
from astropy.units.quantity import Quantity
from tomlkit.toml_file import TOMLFile

from .data_format import DataClass


def obsfile_parser(path: os.PathLike) -> Dict[str, Any]:
    """Observation parameters from alpaca style .obs file.

    Parameters
    ----------
    path
        Path to the .obs file.

    Examples
    --------
    >>> obsfile_parser('test/horizon.obs')
    {'offset_Az': 0, ..., 'script': '200GHz/line_otf_car_rsky.alp'}

    """
    with open(os.path.abspath(path)) as f:
        content = f.read()
    content = re.sub(r"[\t ]*?#.*?\n", r"\n", content)
    # Remove tabs and comment sections.
    content = re.sub(r"(\n.*?);(.*?)\n", r'\1="\2"\n', content)
    # Make format of ``script`` parameter the same as others.

    # Get filename.
    file_name = Path(path).stem
    # build and execute the module
    spec = importlib.util.spec_from_loader(file_name, loader=None)
    pymodule = importlib.util.module_from_spec(spec)
    exec(content, pymodule.__dict__)
    ret = {k: v for k, v in pymodule.__dict__.items() if not k.startswith("__")}
    return ret


class ObsParams(DataClass):
    """Parse observation parameters."""

    def __init__(self, **kwargs):
        """Make Quantity.

        Parameters given as toml-array are converted into ``Quantity`` objects.

        """
        kwargs = self._make_quantity(kwargs)
        super().__init__(**kwargs)

    @classmethod
    def from_file(cls, path: os.PathLike):
        """Parse toml file.

        Parameters
        ----------
        path
            Path to the parameter file.

        Notes
        -----
        All parameters declared in the toml file will be parsed. Table
        names are ignored.

        """
        _params = TOMLFile(path).read()
        params = {}
        for subdict in _params.values():
            params.update({k: v for k, v in subdict.items()})
        return cls(**params)

    @staticmethod
    def _make_quantity(parameters: Dict[str, Any]):
        parsed = {}
        for name, value in parameters.items():
            if value == {}:
                pass
            elif name.isupper():
                parsed[name] = value
            elif name.islower():
                parsed[name] = Quantity(value)
            else:
                parsed[name] = Angle(value)
        return parsed
