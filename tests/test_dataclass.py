import pytest
from n_const.data_format import DataClass


class TestConstants:
    def test_getattr(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            const = DataClass(**kwargs)
            for k, v in kwargs.items():
                assert getattr(const, k) == v

    def test_getitem(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            const = DataClass(**kwargs)
            for k, v in kwargs.items():
                assert const[k] == v

    def test_keys(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert DataClass(**kwargs).keys() == kwargs.keys()

    def test_values(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert list(DataClass(**kwargs).values()) == list(kwargs.values())

    def test_items(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert DataClass(**kwargs).items() == kwargs.items()

    def test_get(self):
        example = DataClass(a=1, b=2)
        assert example.get("a") == 1
        assert example.get("b", 1) == 2
        assert example.get("c") is None
        assert example.get("c", 100) == 100

    def test_pop(self):
        example = DataClass(a=1, b=2)
        assert example.pop("a") == 1
        assert ["b"] == list(example.keys())
        with pytest.raises(KeyError):
            _ = example.pop("a")
        assert example.pop("a", 100) == 100
