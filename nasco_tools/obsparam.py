#!/usr/bin/env python3

import re
import os
import importlib


def obsfile_parser(path):
    with open(os.path.abspath(path)) as f:
        content = f.read()
    content = re.sub(r"\n[^=]*?\n", r"\n\n", content)  # omit non-substitute line
    # get filename
    file_name = os.path.basename(path).split(".")[0]
    # build and execute the module
    spec = importlib.util.spec_from_loader(file_name, loader=None)
    pymodule = importlib.util.module_from_spec(spec)
    exec(content, pymodule.__dict__)
    # remove builtin function mappings
    pymodule.__dict__.pop("__builtins__", None)
    return pymodule.__dict__
