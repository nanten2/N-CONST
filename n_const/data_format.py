from collections.abc import ItemsView, KeysView, ValuesView
from types import SimpleNamespace
from typing import Any, Hashable, Iterator, Tuple


class DataClass(SimpleNamespace):
    r"""Storage of constant values.

    Both attribute access and dict-like key access are supported. Dict methods are
    almost fully supported except ``[fromkeys|setdefault]``.

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

    def __repr__(self) -> str:
        return super().__repr__().replace("namespace", self.__class__.__name__)

    def __len__(self) -> int:
        """Equivalent to ``dict.__len__()`` method."""
        return len(self.__dict__)

    def __getitem__(self, name: Hashable) -> Any:
        """Support value extraction using dict[key] format."""
        return self.__dict__[name]

    def __setitem__(self, name: Hashable, value: Any) -> None:
        """Support value assignment using dict[key] = value format."""
        self.__dict__[name] = value

    def __delitem__(self, name: Hashable) -> None:
        """Equivalent to ``dict.__delitem__`` method."""
        del self.__dict__[name]

    def __contains__(self, key: Hashable) -> bool:
        """Equivalent to ``dict.__contains__()`` method."""
        return key in self.__dict__

    def __iter__(self) -> Iterator[Hashable]:
        """Equivalent to ``dict.__iter__()`` method."""
        return iter(self.__dict__)

    def clear(self) -> None:
        """Equivalent to ``dict.clear()`` method."""
        self.__dict__.clear()

    def copy(self) -> "DataClass":
        """Equivalent to ``dict.copy()`` method."""
        return self.__class__(**self.__dict__.copy())

    def get(self, key: Hashable, default: Any = None) -> Any:
        """Equivalent to ``dict.get(key, default)`` method."""
        return self.__dict__.get(key, default)

    def items(self) -> ItemsView:
        """Equivalent to ``dict.items()`` method."""
        return self.__dict__.items()

    def keys(self) -> KeysView:
        """Equivalent to ``dict.keys()`` method."""
        return self.__dict__.keys()

    def pop(self, key: Hashable, default: Any = KeyError) -> Any:
        """Equivalent to ``dict.pop(key, default)`` method."""
        if default is KeyError:
            return self.__dict__.pop(key)
        else:
            return self.__dict__.pop(key, default)

    def popitem(self) -> Tuple[Hashable, Any]:
        """Equivalent to ``dict.popitem()`` method."""
        return self.__dict__.popitem()

    def __reversed__(self) -> Iterator[Hashable]:
        """Equivalent to ``dict.__reversed__()`` method."""
        return reversed(self.__dict__)

    def update(self, other: "DataClass") -> None:
        """Equivalent to ``dict.update()`` method."""
        self.__dict__.update(other.__dict__)

    def values(self) -> ValuesView:
        """Equivalent to ``dict.values()`` method."""
        return self.__dict__.values()

    def __eq__(self, other: "DataClass") -> bool:
        """Equivalent to ``dict.__eq__()`` method."""
        return self.__dict__ == other.__dict__

    def __ne__(self, other: "DataClass") -> bool:
        """Equivalent to ``dict.__ne__()`` method."""
        return self.__dict__ != other.__dict__
