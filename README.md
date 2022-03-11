# N-CONST

[![PyPI](https://img.shields.io/pypi/v/n-const.svg?label=PyPI&style=flat-square)](https://pypi.org/pypi/n-const/)
[![Python](https://img.shields.io/pypi/pyversions/n-const.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/pypi/n-const/)
[![Test](https://img.shields.io/github/workflow/status/nanten2/N-const/Test?logo=github&label=Test&style=flat-square)](https://github.com/nanten2/NASCO-tools/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](LICENSE)

Necst Constants and ObservatioN Specification Translator.

## Features

This library provides:

- constants of the telescope system as useful python objects
- parsers for parameter files unique to NECST

## Installation

```shell
pip install n-const
```

## Usage

Be careful of the package name! Use underscore instead of hyphen.

### Constants

Solid constants such as location of the telescope are declared in `constants` module. To use the constants:

```python
>>> import n_const
>>> n_const.LOC_NANTEN2
EarthLocation(2230866.39573496, -5440247.68222275, -2475554.41874542) m
>>> n_const.XFFTS.ch_num
32768
```

`Constants` objects support both keys and dot notations to access its components. So you can write:

```python
>>> n_const.XFFTS['ch_num']
32768
```

You now can get all the parameters packed in the `Constants` using `dict` method:

```python
>>> n_const.XFFTS.keys()
dict_keys(['ch_num', 'bandwidth'])
>>> n_const.REST_FREQ.values()
dict_values([<Quantity 115.27 GHz>, <Quantity 110.20 GHz>, ..., <Quantity 219.56 GHz>])
>>> n_const.XFFTS.items()
dict_items([('ch_num', 32768), ('bandwidth', <Quantity 2. GHz>)])
```

### Parameters

Pointing error parameter (parameters to correct pointing error) and observation parameters are extracted via `pointing` and `obsparam` modules respectively.

To get the pointing error parameters:

```python
>>> from n_const.pointing import PointingError
>>> params = PointingError.from_file("path/to/param_file")
>>> params.dAz
Quantity 5314.24667547 arcsec

# This module also supports keys to access the components:

>>> params['dAz']
Quantity 5314.24667547 arcsec
```

To get the observation parameters:

```python
>>> from n_const import obsparams
>>> params = obsparams.OTFParams.from_file("path/to/obs_file")
>>> params.Beta_on
<Angle 15.51638889 deg>
>>> params['Beta_on']
<Angle 15.51638889 deg>
```

For conventional style obsfiles, this module provides a parser. This is a conventional one, so it provides very limited functionality;

- Dot notation is not supported, keys only.
- Return values are not combined with units.

```python
>>> params = obsparams.obsfile_parser("path/to/obs_file")
>>> params['offset_Az']
0
```

---

This library is using [Semantic Versioning](https://semver.org).
