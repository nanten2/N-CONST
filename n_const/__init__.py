# flake8: noqa

try:
    from importlib_metadata import version
except ImportError:
    from importlib.metadata import version  # Python 3.8+

try:
    __version__ = version("n_const")
except:
    __version__ = "0.0.0"  # Fallback.

# Modules
from . import constants
from . import pointing
from . import obsparams

# Aliases
from .constants import *
from .pointing import *
from .obsparams import *

from . import deprecated

# Compatibility
kisa = pointing
kisa.Kisa = deprecated.Kisa
kisa.OpticalKisa = deprecated.OpticalKisa
kisa.RadioKisa = deprecated.RadioKisa
