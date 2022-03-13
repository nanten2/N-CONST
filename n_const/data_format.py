from collections.abc import ItemsView, KeysView, ValuesView
from types import SimpleNamespace
from typing import Any, Hashable


class DataClass(SimpleNamespace):
    r"""Storage of constant values.

    Parameters
    ----------
    kwargs
        Arbitrary number of parameters in ``key=value`` format.

    Examples
    --------
    >>> param = DataClass(a=50, b="abc")
    >>> param.a
    50
    >>> param["b"]
    'abc'

    """

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    def __getitem__(self, name: str) -> Any:
        """Support value extraction using dict[key] format."""
        return self.__dict__[name]

    def __repr__(self) -> str:
        return super().__repr__().replace("namespace", self.__class__.__name__)

    def keys(self) -> KeysView:
        """Equivalent to ``dict.keys()`` method."""
        return self.__dict__.keys()

    def values(self) -> ValuesView:
        """Equivalent to ``dict.values()`` method."""
        return self.__dict__.values()

    def items(self) -> ItemsView:
        """Equivalent to ``dict.items()`` method."""
        return self.__dict__.items()

    def get(self, key: Hashable, default: Any = None) -> Any:
        """Equivalent to ``dict.get(key, default)`` method."""
        return self.__dict__.get(key, default)

    def pop(self, key: Hashable, default: Any = KeyError) -> Any:
        """Equivalent to ``dict.pop(key, default)`` method."""
        if default is KeyError:
            return self.__dict__.pop(key)
        else:
            return self.__dict__.pop(key, default)
