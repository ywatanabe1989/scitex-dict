#!/usr/bin/env python3

"""Dictionary utilities (DotDict, safe_merge) for the SciTeX ecosystem."""

from ._DotDict import DotDict
from ._flatten import flatten
from ._listed_dict import listed_dict
from ._pop_keys import pop_keys
from ._replace import replace
from ._safe_merge import safe_merge
from ._to_str import to_str

__all__ = [
    "DotDict",
    "listed_dict",
    "pop_keys",
    "replace",
    "safe_merge",
    "to_str",
    "flatten",
]
