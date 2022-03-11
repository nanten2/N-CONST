"""Deprecated items, kept for compatibility."""

import os

from .data_format import DataClass
from .pointing import PointingError


class Constants(DataClass):
    """Fundamental class to declare arbitrary parameters.

    .. deprecated:: 1.0.1

        ``n_const.constants.Constants`` will be removed in N-CONST 2.0.0, it's replaced
        by ``n_const.data_format.Constants`` because this module should be more like
        config file.

    Parameters
    ----------
    kwargs
        Any parameter(s) in ``name=value`` style.

    """

    @classmethod
    def set_values(cls, **kwargs):
        """Set arbitrary parameters.

        .. deprecated:: 1.0.1

           ``set_values`` will be removed in N-CONST 2.0.0, it's replaced by class
           constructor ``Constants(**kwargs)`` because this method is not intuitive and
           value protection not necessarily be this hard.

        Parameters
        ----------
        kwargs: Any
            Any parameter(s) in ``name=value`` style.

        Examples
        --------
        >>> params = Constants.set_values(param1=1, param2='a')
        >>> params.param1
        1
        >>> params["param2"]
        'a'
        """
        return cls(**kwargs)

    @classmethod
    def from_csv(cls, path: os.PathLike):
        """Read CSV file and create Constants.
        User defined constants. Intended to be used in __init__.py of the packages that
        depends on this package.

        .. deprecated:: 1.0.1

            ``from_csv`` will be removed in N-CONST 2.0.0, the successor won't be
            implemented because resolving paths to config files can be problematic.

        Parameters
        ----------
        name: str
            The name of the Constants instance.
        path: PathLike
            Path to the CSV file.

        Notes
        -----
        The CSV file is expected to have the following structure;
        ```
        col_name1,col_name2,col_name3 ...
        row_name1,value_2-1,value_3-1 ...
        row_name2,value_2-2,value_3-2 ...
        ```
        Note that column 1 is identical to the row labels.

        """
        raise NotImplementedError
        # with Path(path).open("r", newline="") as f:
        #     contents = csv.DictReader(f)
        #     fields = contents.fieldnames
        #     contents_dict = {}
        #     for row in contents:
        #         contents_dict[row[fields[0]]] = cls.set_values(**row)
        # return cls.set_values(**contents_dict)


Kisa = PointingError
RadioKisa = Kisa
OpticalKisa = Kisa
