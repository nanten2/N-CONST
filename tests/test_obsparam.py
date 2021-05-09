import astropy.units as u
from astropy.units import Quantity
from astropy.coordinates import Angle

from n_const import obsparams

horizontal_obsparams = {
    "offset_Az": 0,
    "offset_El": 0,
    "lambda_on": 83.80613,
    "beta_on": -5.37432,
    "lambda_off": 82.559,
    "beta_off": -5.6683,
    "coordsys": "HORIZONTAL",
    "object": "OriKL",
    "vlsr": 0.0,
    "tuning_vlsr": 0.0,
    "cosydel": "HORIZONTAL",
    "otadel": "N",
    "start_pos_x": -120.0,
    "start_pos_y": -120.0,
    "scan_direction": 0,
    "exposure": 0.6,
    "otfvel": 50.0,
    "otflen": 5.3999999999999995,
    "grid": 30,
    "N": 9,
    "lamdel_off": 0,
    "betdel_off": 0,
    "otadel_off": "N",
    "nTest": 1,
    "datanum": 9.0,
    "lamp_pixels": 4,
    "exposure_off": 10.0,
    "observer": "amigos",
    "obsmode": "LINEOTF",
    "purpose": 2,
    "tsys": 0,
    "acc": 10,
    "load_interval": 5,
    "cold_flag": "N",
    "pllref_if": 1,
    "multiple": 12,
    "pllharmonic": 1,
    "pllsideband": -1,
    "pllreffreq": 0,
    "restfreq_1": 230538.0,
    "obsfreq_1": 230538.0,
    "molecule_1": "12CO",
    "transiti_1": "J=2-1",
    "lo1st_sb_1": "U",
    "if1st_freq_1": 4438.0,
    "lo2nd_sb_1": "L",
    "lo3rd_sb_1": "L",
    "lo3rd_freq_1": 4100.0,
    "if3rd_freq_1": 500.0,
    "start_ch_1": 0,
    "end_ch_1": 16383,
    "restfreq_2": 220398.684,
    "obsfreq_2": 220398.684,
    "molecule_2": "13CO",
    "transiti_2": "J=2-1",
    "lo1st_sb_2": "L",
    "if1st_freq_2": 5701.3,
    "lo2nd_sb_2": "L",
    "lo3rd_sb_2": "L",
    "lo3rd_freq_2": 4100.0,
    "if3rd_freq_2": 500.0,
    "start_ch_2": 0,
    "end_ch_2": 16383,
    "fpga_integtime": 100,
    "script": "200GHz/line_otf_car_rsky.alp",
}

example_toml_obsparams = {
    "scan_direction": "X",
    "n": Quantity(30),
    "scan_spacing": 60 * u.arcsec,
    "otfvel": 600 * u.arcsec / u.s,
    "otflen": 10 * u.s,
    "integ_on": 0.1 * u.s,
    "ramp_pixel": 40,
    "Lambda_on": Angle("3h15m8s"),
    "Beta_on": Angle("15d30m59s"),
    "Lambda_off": Angle("3h50m46s"),
    "Beta_off": Angle("17d25m9s"),
    "coordsys": "J2000",
    "otadel": True,
    "position_angle": 30 * u.deg,
    "start_pos_x": 120 * u.arcsec,
    "start_pos_y": 120 * u.arcsec,
    "integ_off": 10 * u.s,
    "integ_hot": 10 * u.s,
    "off_interval": Quantity(1),
    "load_interval": 5 * u.min,
    "molecule_1": "12CO10",
    "object": "OriKL",
    "observer": "amigos",
}


def test_parser():
    returned = obsparams.obsfile_parser("tests/horizon.obs")
    expected = horizontal_obsparams
    assert returned == expected


def test_OTFParams():
    executed = obsparams.ObsParams.from_file("tests/example.obs.toml")  # noqa: F841
    expected = example_toml_obsparams
    for param, value in expected.items():
        assert eval(f"executed.{param}") == value
        assert executed[param] == value
