r"""Parse pointing error parameters.

Pointing error is corrected by the following equation:

.. math::

    \Delta x =& \chi \sin ( \omega - Az ) \sin ( El ) \\
    &+ \epsilon \sin ( El ) \\
    &+ \chi_2 \sin ( 2 ( \omega_2 - Az ) ) \sin ( El ) \\
    &+ \mathrm{d}Az \cos ( El ) \\
    &+ \mathrm{d}e \\
    &+ \mathrm{cor}_v \cos ( El + \mathrm{cor}_p ) \\
    &+ \mathrm{d}e_\mathrm{radio} \\
    \Delta Az =& \Delta x / \cos ( El ) \\
    \Delta y =& - \chi \cos ( \omega - Az ) \\
    &- \chi_2 \cos ( 2 ( \omega_2 - Az ) ) \\
    &+ g_1 \cos ( El ) + g_2 \sin ( El ) \\
    &+ \mathrm{d} el \\
    &+ g_{ 1,\mathrm{radio} } \cos ( El ) + g_{ 2,\mathrm{radio} } \sin ( El ) \\
    &- \mathrm{cor}_v \sin ( El + \mathrm{cor}_p ) \\
    &+ \mathrm{d}el_\mathrm{radio} \\
    \Delta El =& \Delta y

"""

__all__ = ["PointingError"]

import os
from typing import Any, Dict

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated  # For Python<3.9

import astropy.units as u
from tomlkit.toml_file import TOMLFile

from .data_format import DataClass


class PointingError(DataClass):
    """Errors of telescope and its system installation.

    Notes
    -----
    All quantities with [arcsec] are offset or inclination of somewhere
    in the system. Quantities with [deg] are phases of offsets.
    Quantities with [dimensionless] are coefficients of polynomial
    fitting.

    """

    dAz: Annotated[float, u.arcsec] = None
    """Offset of encoder reading."""
    de: Annotated[float, u.arcsec] = None
    """Az offset."""
    chi_Az: Annotated[float, u.arcsec] = None
    """Offset from Az axis inclination."""
    omega_Az: Annotated[float, u.deg] = None
    """Phase of Az axis inclination."""
    eps: Annotated[float, u.arcsec] = None
    """Az-El axes skew angle."""
    chi2_Az: Annotated[float, u.arcsec] = None
    """Offset from 180 deg periodic error."""
    omega2_Az: Annotated[float, u.deg] = None
    """Phase of 180 deg periodic error."""
    chi_El: Annotated[float, u.arcsec] = None
    """Offset from Az axis inclination."""
    omega_El: Annotated[float, u.deg] = None
    """Phase of Az axis inclination."""
    chi2_El: Annotated[float, u.arcsec] = None
    """Offset from 180 deg periodic error."""
    omega2_El: Annotated[float, u.deg] = None
    """Phase of 180 deg periodic error."""
    g: Annotated[float, u.dimensionless_unscaled] = None
    """Optical gravitational deflection."""
    gg: Annotated[float, u.dimensionless_unscaled] = None
    """Optical gravitational deflection."""
    ggg: Annotated[float, u.dimensionless_unscaled] = None
    """Optical gravitational deflection."""
    gggg: Annotated[float, u.dimensionless_unscaled] = None
    """Optical gravitational deflection."""
    dEl: Annotated[float, u.arcsec] = None
    """Offset of encoder reading."""
    de_radio: Annotated[float, u.arcsec] = None
    """Az offset."""
    dEl_radio: Annotated[float, u.arcsec] = None
    cor_v: Annotated[float, u.arcsec] = None
    """Offset from collimation error."""
    cor_p: Annotated[float, u.deg] = None
    """Phase of collimation error."""
    g_radio: Annotated[float, u.dimensionless_unscaled] = None
    """Radio gravitational deflection."""
    gg_radio: Annotated[float, u.dimensionless_unscaled] = None
    """Radio gravitational deflection."""
    ggg_radio: Annotated[float, u.dimensionless_unscaled] = None
    """Radio gravitational deflection."""
    gggg_radio: Annotated[float, u.dimensionless_unscaled] = None
    """Radio gravitational deflection."""

    def __init__(self, **kwargs) -> None:
        kwargs = self._make_quantity(kwargs)
        super().__init__(**kwargs)

    def _make_quantity(self, parameters: Dict[str, Any]) -> Dict[str, u.Quantity]:
        for (name, field_type) in self.__annotations__.items():
            try:
                parameters[name] *= field_type.__metadata__[0]
            except TypeError:
                raise ValueError(f"Parameter {name} should be given via kisa-file.")
        return parameters

    @classmethod
    def from_file(cls, path: os.PathLike, key: str = "pointing_params"):
        """Parse toml file.

        Parameters
        ----------
        path
            Path to pointing error parameter file.
        key
            Table name in the TOML file.

        """
        params = TOMLFile(path).read()
        return cls(**params[key])
