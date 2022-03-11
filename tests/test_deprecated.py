from n_const.deprecated import Constants


class TestConstants:
    def test_set_values(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert Constants.set_values(**kwargs) == Constants(**kwargs)

    def test_from_csv(self):
        # Not working.
        pass
