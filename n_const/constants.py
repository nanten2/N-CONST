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


# Location
LOC_NANTEN2 = EarthLocation(
    lon=-67.70308139 * u.deg,
    lat=-22.96995611 * u.deg,
    height=4863.85 * u.m,
)

# Spectrometer
XFFTS = Constants.set_values(ch_num=32768, bandwidth=2 * u.GHz)
AC240 = Constants.set_values(ch_num=16384, bandwidth=1 * u.GHz)

# Rest frequency
REST_FREQ = Constants.set_values(
    j10_12co=115.271202 * u.GHz,
    j10_13co=110.201353 * u.GHz,
    j10_c18o=109.782173 * u.GHz,
    j21_12co=230.538000 * u.GHz,
    j21_13co=220.398681 * u.GHz,
    j21_c18o=219.560354 * u.GHz,
    # reference: Naomasa Nakai et al. 2009, ISBN978-4-535-60766-8
)


if __name__ == "__main__":
    pass
