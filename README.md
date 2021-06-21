# N-CONST

[![PyPI](https://img.shields.io/pypi/v/n-const.svg?label=PyPI&style=flat-square)](https://pypi.org/pypi/n-const/)
[![Python](https://img.shields.io/pypi/pyversions/n-const.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/pypi/n-const/)
[![Test](https://img.shields.io/github/workflow/status/nanten2/N-const/Test?logo=github&label=Test&style=flat-square)](https://github.com/nanten2/NASCO-tools/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](LICENSE)

NANTEN2/NASCO Constants and ObservatioN Specification Translator.

## Features

This library provides:

- constants of the telescope system as useful python objects
- parsers for parameter files unique to NANTEN2/NASCO system

## Installation

```shell
pip install n-const
```

## Usage

Be careful of the package name! Use underscore instead of hyphen.

### Constants

Solid constants such as location of the telescope are declared in `constants` module. To use the constants:

```python
>>> import n_const.constants as n2const
>>> n2const.LOC_NANTEN2
EarthLocation(2230866.39573496, -5440247.68222275, -2475554.41874542) m
>>> n2const.XFFTS.ch_num
32768
```

`Constants` objects support both keys and dot notations to access its components. So you can write:

```python
>>> n2consst.XFFTS['ch_num']
32768
```

You now can get all the parameters packed in the `Constants` using `dict` method:

```python
>>> n2const.XFFTS.keys()
dict_keys(['ch_num', 'bandwidth'])
>>> n2const.REST_FREQ.values()
dict_values([<Quantity 115.27 GHz>, <Quantity 110.20 GHz>, ..., <Quantity 219.56 GHz>])
>>> n2const.XFFTS.items()
dict_items([('ch_num', 32768), ('bandwidth', <Quantity 2. GHz>)])
```

### Parameters

*Kisa* parameter (parameters to correct pointing error) and observation parameters are extracted via `kisa` and `obsparam` modules respectively.

To get the *kisa* parameters:

```python
>>> from n_const import kisa
>>> params = kisa.RadioKisa.from_file("path/to/kisafile")
>>> params.dAz
Quantity 5314.24667547 arcsec

# This module also supports keys to access the components:

>>> params['dAz']
Quantity 5314.24667547 arcsec
```

To get the observation parameters:

```python
>>> from n_const import obsparams
>>> params = obsparams.OTFParams.from_file("path/to/obsfile")
>>> params.Beta_on
<Angle 15.51638889 deg>
>>> params['Beta_on']
<Angle 15.51638889 deg>
```

For conventional style obsfiles, this module provides a parser. This is a conventional one, so it provides very limited functionality;

- Dot notation is not supported, keys only.
- Return values are not combined with units.

```python
>>> params = obsparams.obsfile_parser("path/to/obsfile")
>>> params['offset_Az']
0
```

---

This library is using [Semantic Versioning](https://semver.org).
