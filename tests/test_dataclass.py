import sys

import pytest
from n_const.data_format import DataClass

PYTHON_VERSION = sys.version_info


class TestDataClass:
    def test_repr(self):
        data = DataClass(a=1, b=2)
        assert repr(data) == "DataClass(a=1, b=2)"

    def test_getattr(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            data = DataClass(**kwargs)
            for k, v in kwargs.items():
                assert getattr(data, k) == v

    def test_len(self):
        test_cases = [
            {},
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert len(DataClass(**kwargs)) == len(kwargs)

    def test_getitem(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            data = DataClass(**kwargs)
            for k, v in kwargs.items():
                assert data[k] == v

    def test_setitem(self):
        data = DataClass()
        data["a"] = 1
        assert data["a"] == 1
        data["b"] = 2
        assert data["b"] == 2
        data["a"] = "1"
        assert data["a"] == "1"

    def test_delitem(self):
        data = DataClass(a=1, b=2)
        del data["a"]
        with pytest.raises(KeyError):
            assert data["a"] == 1
        assert data["b"] == 2

    def test_contains(self):
        data = DataClass(a=1, b=2)
        assert "a" in data
        assert "b" in data
        assert "c" not in data

    def test_iter(self):
        data = DataClass(a=1, b=2)

        assert list(iter(data)) == ["a", "b"]

        keys = [k for k in data]
        assert keys == ["a", "b"]

    def test_clear(self):
        data = DataClass(a=1, b=2)
        data.clear()
        assert list(data.keys()) == []

    def test_copy(self):
        data = DataClass(a=1, b=2)
        copied = data.copy()
        assert data == copied
        assert data is not copied

    def test_get(self):
        example = DataClass(a=1, b=2)
        assert example.get("a") == 1
        assert example.get("b", 1) == 2
        assert example.get("c") is None
        assert example.get("c", 100) == 100

    def test_items(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert DataClass(**kwargs).items() == kwargs.items()

    def test_keys(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert DataClass(**kwargs).keys() == kwargs.keys()

    def test_pop(self):
        example = DataClass(a=1, b=2)
        assert example.pop("a") == 1
        assert ["b"] == list(example.keys())
        with pytest.raises(KeyError):
            _ = example.pop("a")
        assert example.pop("a", 100) == 100

    def test_popitem(self):
        data = DataClass(a=1, b=2)
        assert data.popitem() == ("b", 2)
        assert data.popitem() == ("a", 1)

    @pytest.mark.skipif(
        PYTHON_VERSION < (3, 8),
        reason="Reversing dict object isn't supported for Python < 3.8",
    )
    def test_reversed(self):
        data = DataClass(a=1, b=2)
        assert list(reversed(data)) == ["b", "a"]

    def test_update(self):
        data = DataClass(a=1, b=2)
        additional = DataClass(b=5, c=10)
        data.update(additional)
        assert data == DataClass(a=1, b=5, c=10)

    def test_values(self):
        test_cases = [
            {"a": 1},
            {"a": 1, "b": 2},
            {"a": "1", "b": 2},
        ]
        for kwargs in test_cases:
            assert list(DataClass(**kwargs).values()) == list(kwargs.values())

    def test_eq_ne(self):
        assert DataClass() == DataClass()
        assert DataClass() != DataClass(a=1)
        assert DataClass(a=1, b=2) == DataClass(a=1, b=2)
        assert DataClass(a=1, b=2) != DataClass(a="1", b=2)
        assert DataClass(a=1, b=2) != DataClass(a=2, b=2)
