import astropy.units as u

from nasco_tools import kisa

kisa_expected = {
    "dAz": 5314.2466754691195 * u.arcsec,
    "de": 382 * u.arcsec,
    "chi_Az": -27.743114809726713 * u.arcsec,
    "omega_Az": -10.004233550100272 * u.deg,
    "eps": -13.562343977659976 * u.arcsec,
    "chi2_Az": -3.2283345930067489 * u.arcsec,
    "omega2_Az": -34.73486665318979 * u.deg,
    "chi_El": -30.046387189617871 * u.arcsec,
    "omega_El": -16.233694100299584 * u.deg,
    "chi2_El": -1.1446000035021269 * u.arcsec,
    "omega2_El": -41.474874481601418 * u.deg,
    "g": -0.17220574801726421 * u.dimensionless_unscaled,
    "gg": 0.0 * u.dimensionless_unscaled,
    "ggg": 0.0 * u.dimensionless_unscaled,
    "gggg": 0.0 * u.dimensionless_unscaled,
    "dEl": 6520.2376117807198 * u.arcsec,
    "de_radio": -394.46 * u.arcsec,
    "dEl_radio": 210.7228 * u.arcsec,
    "cor_v": 27.434 * u.arcsec,
    "cor_p": -31.6497 * u.deg,
    "g_radio": -0.454659 * u.dimensionless_unscaled,
    "gg_radio": 0.0128757 * u.dimensionless_unscaled,
    "ggg_radio": 0.000000 * u.dimensionless_unscaled,
    "gggg_radio": 0.000000 * u.dimensionless_unscaled,
}


def test_RadioKisa():
    executed = kisa.RadioKisa.from_file("test/hosei_230.toml")  # noqa: F841
    expected = kisa_expected
    for param, value in expected.items():
        assert eval(f"executed.{param}") == value
        assert executed[param] == value
