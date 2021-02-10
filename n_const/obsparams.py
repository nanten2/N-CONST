#!/usr/bin/env python3

import re
import os
import importlib
from dataclasses import dataclass

from astropy.units.quantity import Quantity
import toml


def obsfile_parser(path):
    """Observation parameters from alpaca style .obs file.
    Parameters
    ----------
    path: str

    Examples
    --------
    >>> obsfile_parser('test/horizon.obs')  # doctest: +NORMALIZE_WHITESPACE
    {'offset_Az': 0, 'offset_El': 0, 'lambda_on': 83.80613,\
    'beta_on': -5.37432, 'lambda_off': 82.559, 'beta_off': -5.6683,\
    'coordsys': 'HORIZONTAL', 'object': 'OriKL', 'vlsr': 0.0,\
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
class ObsParams(object):
    """Metaclass for obsparam dataclasses.

    Notes
    -----
    This class is meant to be inherited.
    """

    def __post_init__(self):
        """Make Quantity.
        Parameters given as toml-array are converted into `Quantity` objects.
        """
        for name, attr in self.__dict__.items():
            if isinstance(attr, list):
                self.__dict__[name] = Quantity(" ".join(attr))
        return

    @classmethod
    def from_file(cls, path):
        """Parse toml file.

        Parameters
        ----------
        path: str

        Notes
        -----
        Non-standard parameters will also parsed.
        """
        params = toml.load(f"{os.path.abspath(path)}")
        mode = list(params.keys())[0]
        # if parameters in toml file is strictly limited, following 6 lines can
        # be omitted, and the following would be `inst = cls(**params[mode])`
        declared, notdeclared = {}, {}
        for param, value in params[mode].items():
            if param not in cls.__annotations__.keys():
                notdeclared[param] = value
            else:
                declared[param] = value
        inst = cls(**declared)
        object.__setattr__(inst, "mode", mode)
        # following 3 lines will also be omitted
        for param, value in notdeclared.items():
            object.__setattr__(inst, param, value)
        # to convert not-declared parameters to Quantity obj
        inst.__post_init__()  # not efficient way though,,,
        return inst

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass(frozen=True)
class OTFParams(ObsParams):
    """Parameters for OTF observation.

    Examples
    --------
    >>> param = OTFParams.from_file('test/horizon.obs.toml')
    >>> param.offset_Az
    <Quantity 0. deg>

    Attributes
    ----------
    offset_Az: Quantity
        ??? Horizontal offset.
    offset_El: Quantity
        ??? Horizontal offset.
    lambda_on: Quantity
        x coordinate of ON position.
    beta_on: Quantity
        y coordinate of ON position.
    lambda_off: Quantity
        x coordinate of OFF position.
    beta_off: Quantity
        y coordinate of OFF position.
    coordsys: str
        Coordinate system, ['j2000', 'b1950', 'galactic']
    Object: str
        Name of target.
    vlsr: Quantity
        Object's velocity relative to LSR frame.
    tuning_vlsr: Quantity
        ???
    cosydel: str
        Coordinate of map offset, ['j2000', 'b1950', 'galactic', 'hoizontal']
    otadel: str  # -> bool
        Correction flag of map offset. [Y/N]
    start_pos_x: Quantity
        x start position.
    start_pos_y: Quantity
        y start position.
    scan_direction: str  # -> ?
        Direction of scan. ['0':x, '1':y]
    exposure: Quantity
        Integration time, should be >= 0.04 sec.
    otfvel: Quantity
        Angular velocity of OTF scan.
    otflen: Quantity
        ??? needed?
    grid: Quantity
        ??? resolution?
    N: int
        Number of scan lines.
    lamdel_off: Quantity
        x coordinate of OFF point offset.
    betdel_off: Quantity
        y coordinate of OFF point offset.
    otadel_off: str  # -> bool
        Correction flag of OFF point offset. [Y/N]
    nTest: int
        Number of observation sequence.
    datanum: int
        Number of data.
    lamp_pixels: int
        Number of pixels used as run-up ramp.
    exposure_off: Quantity
        Exposure on OFF point.
    observer: str
        Name of observer.
    obsmode: str
        Observation mode. ['LINEPSSW', 'LINEOTF', ...]
    purpose: str  # appropreate?
        Observation purpose. ['0':normal, '1':pointing, '2':calibration]
    tsys: Quantity
        System noise temperature.
    acc: Quantity
        Tracking accuracy.
    load_interval: Quantity
        Load measurement interval.
    cold_flag: str  # -> bool?
        Cold load measurement flag.
    pllref_if: int  # str?
        ??? Phase lock loop. ['1':IF1, '2':IF2]
    multiple: Quantity
        Factor of frequency multiplier.
    pllharmonic: str  # ?
        ??? Factor of frequency multiplier for PLL.
    pllsideband: str  # appropreate?
        PLL sideband. ['1', '-1']
    pllreffreq: Quantity
        PLL reference frequency.
    restfreq_1: Quantity
        Rest frequency.
    obsfreq_1: Quantity
        ??? Observed frequency.
    molecule_1: Quantity
        ??? Identify target molecule.
    transiti_1: str
        ??? Identify target transition.
    lo1st_sb_1: str
        Sideband considering 1st LO.
    if1st_freq_1: Quantity
        IF frequency after conversion by 1st LO.
    lo2nd_sb_1: str
        Sideband considering 2nd LO.
    lo3rd_sb_1: str
        ???
    lo3rd_freq_1: Quantity
        ???
    if3rd_freq_1: Quantity
        ???
    start_ch_1: int
        Start channel of spectrometer. <0-based>
    end_ch_1: int
        End channel of spectrometer. <0-based>
    restfreq_2: Quantity
        Rest frequency.
    obsfreq_2: Quantity
        ??? Observed frequency.
    molecule_2: str
        ??? Identify target molecule.
    transiti_2: str
        ??? Identify target transition.
    lo1st_sb_2: str
        Sideband considering 1st LO.
    if1st_freq_2: Quantity
        IF frequency after conversion by 1st LO.
    lo2nd_sb_2: str
        Sideband considering 2nd LO.
    lo3rd_sb_2: str
        ???
    lo3rd_freq_2: Quantity
        ???
    if3rd_freq_2: Quantity
        ???
    start_ch_2: int
        Start channel of spectrometer. <0-based>
    end_ch_2: int
        End channel of spectrometer. <0-based>
    fpga_integtime: Quantity
        FPGA integration time.

    Notes
    -----
    This class cannot be instantiated directly. Use `from_file(path)`.
    """

    offset_Az: Quantity
    offset_El: Quantity
    lambda_on: Quantity
    beta_on: Quantity
    lambda_off: Quantity
    beta_off: Quantity
    coordsys: str
    Object: str  # change to capital because of name conflict
    vlsr: Quantity
    tuning_vlsr: Quantity
    cosydel: str
    otadel: str  # -> bool
    start_pos_x: Quantity
    start_pos_y: Quantity
    scan_direction: str  # -> ?
    exposure: Quantity
    otfvel: Quantity
    otflen: Quantity
    grid: Quantity
    N: int
    lamdel_off: Quantity
    betdel_off: Quantity
    otadel_off: str  # -> bool
    nTest: int
    datanum: int
    lamp_pixels: int
    exposure_off: Quantity
    observer: str
    obsmode: str
    purpose: str  # appropreate?
    tsys: Quantity
    acc: Quantity
    load_interval: Quantity
    cold_flag: str  # -> bool?
    pllref_if: int  # str?
    multiple: Quantity
    pllharmonic: str  # ?
    pllsideband: str  # appropreate?
    pllreffreq: Quantity
    restfreq_1: Quantity
    obsfreq_1: Quantity
    molecule_1: Quantity
    transiti_1: str
    lo1st_sb_1: str
    if1st_freq_1: Quantity
    lo2nd_sb_1: str
    lo3rd_sb_1: str
    lo3rd_freq_1: Quantity
    if3rd_freq_1: Quantity
    start_ch_1: int
    end_ch_1: int
    restfreq_2: Quantity
    obsfreq_2: Quantity
    molecule_2: str
    transiti_2: str
    lo1st_sb_2: str
    if1st_freq_2: Quantity
    lo2nd_sb_2: str
    lo3rd_sb_2: str
    lo3rd_freq_2: Quantity
    if3rd_freq_2: Quantity
    start_ch_2: int
    end_ch_2: int
    fpga_integtime: Quantity


if __name__ == "__main__":
    pass
