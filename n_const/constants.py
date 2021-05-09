#!/usr/bin/env python3
"""Constants unique to NANTEN2/NASCO system.

This module provides static constants of NANTEN2/NASCO system.

Notes
-----
This module provide some ``Constants`` objects. See below for the way to
extract constants from the object.

Examples
--------
>>> params
Constant({'param1': 1})
>>> params['param1']
1
>>> params.param1
1
"""

__all__ = [
    "LOC_NANTEN2",
    "XFFTS",
    "AC240",
    "TOPIC2BEAM",
    "REST_FREQ",
]

from dataclasses import dataclass
import csv

from astropy.coordinates import EarthLocation
import astropy.units as u


@dataclass(frozen=True)
class Constants:
    """Fundamental class to declare arbitrary parameters.

    Notes
    -----
    Use `set_values` method to declare new constants.
    """

    @classmethod
    def set_values(cls, **kwargs):
        """Set arbitrary parameters.

        Parameters
        ----------
        **kwargs: Any
            Any parameter(s) in `name = value` form.

        Examples
        --------
        >>> params = Constants.set_values(param1=1, param2='a')
        >>> params.param1
        1
        >>> params["param2"]
        'a'
        """
        inst = cls()
        for k, v in kwargs.items():
            object.__setattr__(inst, k, v)
        return inst

    def __repr__(self):
        """Show contents."""
        return f"Constants({repr(self.__dict__)})"

    def __getitem__(self, item):
        """Provide key access to parameters."""
        return getattr(self, item)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()


# Location
LOC_NANTEN2 = EarthLocation(
    lon=-67.70308139 * u.deg,
    lat=-22.96995611 * u.deg,
    height=4863.85 * u.m,
)  #: Location of NANTEN2 telescope.

# Spectrometer
XFFTS = Constants.set_values(
    ch_num=32768, bandwidth=2 * u.GHz
)  #: Parameters about XFFTS spectrometer.
AC240 = Constants.set_values(
    ch_num=16384, bandwidth=1 * u.GHz
)  #: Parameters about AC240 spectrometer.

# Board/topic configuration
topic_map = {}
with open("config/board_config.csv", newline="") as f:
    contents = csv.DictReader(f)
    fields = contents.fieldnames
    for row in contents:
        topic_map[row[fields[0]]] = Constants.set_values(**row)
TOPIC2BEAM = Constants.set_values(**topic_map)

# Rest frequency
REST_FREQ = Constants.set_values(
    j10_12co=115.271202 * u.GHz,
    j10_13co=110.201353 * u.GHz,
    j10_c18o=109.782173 * u.GHz,
    j21_12co=230.538000 * u.GHz,
    j21_13co=220.398681 * u.GHz,
    j21_c18o=219.560354 * u.GHz,
    # reference: Naomasa Nakai et al. 2009, ISBN978-4-535-60766-8
)  #: Rest frequencies of CO line emissions.


if __name__ == "__main__":
    pass
