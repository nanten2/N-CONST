from n_const import constants


def test_constants():
    params = constants.Constants.set_values(param1=1, param2="a")
    assert params.param1 == 1
    assert params["param1"] == 1
    assert params.param2 == "a"
    assert params["param2"] == "a"
