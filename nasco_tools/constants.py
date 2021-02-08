#!/usr/bin/env python3

from dataclasses import dataclass

from astropy.coordinates import EarthLocation
import astropy.units as u


@dataclass(frozen=True)
class Constants:
    @classmethod
    def set_values(cls, **kwargs):
        inst = cls()
        for k, v in kwargs.items():
            object.__setattr__(inst, k, v)
        return inst

    def __repr__(self):
        return f"Constant({repr(self.__dict__)})"

    def __getitem__(self, item):
        return getattr(self, item)


LOC_NANTEN2 = EarthLocation(
    lon=-67.70308139 * u.deg,
    lat=-22.96995611 * u.deg,
    height=4863.85 * u.m,
)

XFFTS = Constants.set_values(ch_num=32768, bandwidth=2 * u.GHz)
AC240 = Constants.set_values(ch_num=16384, bandwidth=1 * u.GHz)


if __name__ == "__main__":
    pass
