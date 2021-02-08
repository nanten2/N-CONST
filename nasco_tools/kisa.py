#!/usr/bin/env python3

from dataclasses import dataclass
import os

try:
    from typing_extensions import Annotated
except ImportError:
    from typing import Annotated  # python 3.9 and later

import astropy.units as u
import numpy as np
import toml


@dataclass(frozen=True)
class Kisa(object):
    """Errors of telescope and its system installation.

    Attributes
    ----------
    dAz: Quantity [arcsec]
    dEl: Quantity [arcsec]
        Offset of encoder reading.
    chi_Az: Quantity [arcsec]
    chi_El: Quantity [arcsec]
    omega_Az: Quantity [deg]
    omega_El: Quantity [deg]
        Inclination of Az axis. They should be $chi_Az = chi_El$, $omega_Az = omega_El$.
    chi2_Az: Quantity [arcsec]
    chi2_El: Quantity [arcsec]
    omega2_Az: Quantity [deg]
    omega2_El: Quantity [deg]
        180 deg periodic term. Should be $chi2_Az = chi2_El$, $omega2_Az = omega2_El$.
    de: Quantity [arcsec]
        Inclination of El axis.
    eps: Quantity [arcsec]
        Non-perpendicularity, i.e., angle between AzEl axes, subtracted from 90 deg.
    cor_v: Quantity [arcsec]
    cor_p: Quantity [deg]
        Collimation error.
    g: Quantity [dimensionless]
    gg: Quantity [dimensionless]
    ggg: Quantity [dimensionless]
    gggg: Quantity [dimensionless]
        Gravity effect.
    de_radio: Quantity [arcsec]
    dEl_radio: Quantity [arcsec]
    g_radio: Quantity [dimensionless]
    gg_radio: Quantity [dimensionless]
    ggg_radio: Quantity [dimensionless]
    gggg_radio: Quantity [dimensionless]
        Radio counterparts of aforementioned.

    Notes
    -----
    All quantities with [arcsec] are offset or inclination of somewhere
    in the system. Quantities with [deg] are phases of offsets.
    Quantities with [dimensionless] are coefficients of polynomial
    fitting.
    """

    dAz: Annotated[float, u.arcsec] = None
    de: Annotated[float, u.arcsec] = np.nan
    chi_Az: Annotated[float, u.arcsec] = None
    omega_Az: Annotated[float, u.deg] = None
    eps: Annotated[float, u.arcsec] = None
    chi2_Az: Annotated[float, u.arcsec] = np.nan
    omega2_Az: Annotated[float, u.deg] = np.nan
    chi_El: Annotated[float, u.arcsec] = None
    omega_El: Annotated[float, u.deg] = None
    chi2_El: Annotated[float, u.arcsec] = np.nan
    omega2_El: Annotated[float, u.deg] = np.nan
    g: Annotated[float, u.dimensionless_unscaled] = np.nan
    gg: Annotated[float, u.dimensionless_unscaled] = np.nan
    ggg: Annotated[float, u.dimensionless_unscaled] = np.nan
    gggg: Annotated[float, u.dimensionless_unscaled] = np.nan
    dEl: Annotated[float, u.arcsec] = None
    de_radio: Annotated[float, u.arcsec] = np.nan
    dEl_radio: Annotated[float, u.arcsec] = np.nan
    cor_v: Annotated[float, u.arcsec] = np.nan
    cor_p: Annotated[float, u.arcsec] = np.nan
    g_radio: Annotated[float, u.dimensionless_unscaled] = np.nan
    gg_radio: Annotated[float, u.dimensionless_unscaled] = np.nan
    ggg_radio: Annotated[float, u.dimensionless_unscaled] = np.nan
    gggg_radio: Annotated[float, u.dimensionless_unscaled] = np.nan

    def __post_init__(self):
        for (name, field_type) in self.__annotations__.items():
            try:
                self.__dict__[name] *= field_type.__metadata__[0]
                # if default value np.nan is passed, this won't raise error
                # but if default value None is passed, this raises an error.
            except TypeError:
                raise ValueError(f"Parameter {name} should be given via kisa-file.")
        return

    @classmethod
    def from_file(cls, path):
        params = toml.load(f"{os.path.abspath(path)}")
        return cls(**params["hosei_params"])
    
    def __getitem__(self, item):
        return getattr(self, item)


class RadioKisa(Kisa):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class OpticalKisa(Kisa):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
