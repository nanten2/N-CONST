#!/usr/bin/env python3
"""Parse *kisa* parameters."""

__all__ = ["Kisa", "RadioKisa"]

from dataclasses import dataclass
from pathlib import Path
import os

try:
    from typing_extensions import Annotated
except ImportError:
    from typing import Annotated  # For python 3.9

import astropy.units as u
from tomlkit.toml_file import TOMLFile


@dataclass(frozen=True)
class Kisa:
    """Errors of telescope and its system installation.

    Notes
    -----
    All quantities with [arcsec] are offset or inclination of somewhere
    in the system. Quantities with [deg] are phases of offsets.
    Quantities with [dimensionless] are coefficients of polynomial
    fitting.
    """

    dAz: Annotated[float, u.arcsec] = None  #: Offset of encoder reading.
    de: Annotated[float, u.arcsec] = None  #: Az offset.
    chi_Az: Annotated[float, u.arcsec] = None  #: Offset from Az axis inclination.
    omega_Az: Annotated[float, u.deg] = None  #: Phase of Az axis inclination.
    eps: Annotated[float, u.arcsec] = None  #: Az-El axes skew angle.
    chi2_Az: Annotated[float, u.arcsec] = None  #: Offset from 180 deg periodic error.
    omega2_Az: Annotated[float, u.deg] = None  #: Phase of 180 deg periodic error.
    chi_El: Annotated[float, u.arcsec] = None  #: Offset from Az axis inclination.
    omega_El: Annotated[float, u.deg] = None  #: Phase of Az axis inclination.
    chi2_El: Annotated[float, u.arcsec] = None  #: Offset from 180 deg periodic error.
    omega2_El: Annotated[float, u.deg] = None  #: Phase of 180 deg periodic error.
    g: Annotated[
        float, u.dimensionless_unscaled
    ] = None  #: Optical gravitational deflection.
    gg: Annotated[
        float, u.dimensionless_unscaled
    ] = None  #: Optical gravitational deflection.
    ggg: Annotated[
        float, u.dimensionless_unscaled
    ] = None  #: Optical gravitational deflection.
    gggg: Annotated[
        float, u.dimensionless_unscaled
    ] = None  #: Optical gravitational deflection.
    dEl: Annotated[float, u.arcsec] = None  #: Offset of encoder reading.
    de_radio: Annotated[float, u.arcsec] = None  #: Az offset.
    dEl_radio: Annotated[float, u.arcsec] = None
    cor_v: Annotated[float, u.arcsec] = None  #: Offset from collimation error.
    cor_p: Annotated[float, u.deg] = None  #: Phase of collimation error.
    g_radio: Annotated[
        float, u.dimensionless_unscaled
    ] = None  #: Radio gravitational deflection.
    gg_radio: Annotated[
        float, u.dimensionless_unscaled
    ] = None  #: Radio gravitational deflection.
    ggg_radio: Annotated[
        float, u.dimensionless_unscaled
    ] = None  #: Radio gravitational deflection.
    gggg_radio: Annotated[
        float, u.dimensionless_unscaled
    ] = None  #: Radio gravitational deflection.

    def __post_init__(self):
        for (name, field_type) in self.__annotations__.items():
            try:
                self.__dict__[name] *= field_type.__metadata__[0]
            except TypeError:
                raise ValueError(f"Parameter {name} should be given via kisa-file.")
        return

    @classmethod
    def from_file(cls, path: os.PathLike):
        """Parse toml file.

        Parameters
        ----------
        path: str
        """
        params = TOMLFile(Path(path).absolute()).read()
        return cls(**params["hosei_params"])

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return f"Kisa({repr(self.__dict__)})"

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()


class RadioKisa(Kisa):
    """Kisa-parameters for radio observations.

    Examples
    --------
    >>> kisa = RadioKisa.from_file("test/hosei_230.toml")
    >>> kisa.dAz
    <Quantity 5314.24667547 arcsec>
    >>> kisa['g']
    <Quantity -0.17220575>
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class OpticalKisa(Kisa):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    pass
