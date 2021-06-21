from pathlib import Path

from n_const import constants


def test_constants():
    params = constants.Constants.set_values(param1=1, param2="a")
    assert params.param1 == 1
    assert params["param1"] == 1
    assert params.param2 == "a"
    assert params["param2"] == "a"
    as_dict = {"param1": 1, "param2": "a"}
    assert params.keys() == as_dict.keys()
    assert list(params.values()) == list(as_dict.values())
    assert params.items() == as_dict.items()
    TOPIC2BEAM = constants.Constants.from_csv(Path("tests/board_config.csv"))
    assert TOPIC2BEAM.ac240_tp_data_1.beam == "1"
