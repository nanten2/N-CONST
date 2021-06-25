# flake8: noqa

import pkg_resources


__version__ = pkg_resources.get_distribution("n_const").version

from . import constants
from . import kisa
from . import obsparams
