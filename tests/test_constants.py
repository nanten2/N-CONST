from n_const import Constants


class TestConstants:
    def test_getattr(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            const = Constants(**kwargs)
            for k, v in kwargs.items():
                assert getattr(const, k) == v

    def test_getitem(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            const = Constants(**kwargs)
            for k, v in kwargs.items():
                assert const[k] == v

    def test_keys(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert Constants(**kwargs).keys() == kwargs.keys()

    def test_values(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert list(Constants(**kwargs).values()) == list(kwargs.values())

    def test_items(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert Constants(**kwargs).items() == kwargs.items()
