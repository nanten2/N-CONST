"""Constant parameters used in our telescope systems."""

__all__ = [
    "LOC_NANTEN2",
    "XFFTS",
    "AC240",
    "REST_FREQ",
]

import astropy.units as u
from astropy.coordinates import EarthLocation

from .deprecated import Constants


# Location
LOC_NANTEN2 = EarthLocation(
    lon=-67.70308139 * u.deg, lat=-22.96995611 * u.deg, height=4863.85 * u.m
)
"""Location of NANTEN2 telescope."""
LOC_1p85m = EarthLocation(
    lon=138.472153 * u.deg, lat=35.940874 * u.deg, height=1386 * u.m
)
"""Location of OPU 1.85-m telescope."""

# Spectrometer
XFFTS = Constants(ch_num=32768, bandwidth=2 * u.GHz)
"""Parameters of XFFTS spectrometer."""
AC240 = Constants(ch_num=16384, bandwidth=1 * u.GHz)
"""Parameters of AC240 spectrometer."""

# Rest frequency
REST_FREQ = Constants(
    j10_12co=115.271202 * u.GHz,
    j10_13co=110.201353 * u.GHz,
    j10_c18o=109.782173 * u.GHz,
    j21_12co=230.538000 * u.GHz,
    j21_13co=220.398681 * u.GHz,
    j21_c18o=219.560354 * u.GHz,
)
"""Rest frequencies of CO line emissions. [Ref. ISBN978-4-535-60766-8]"""
