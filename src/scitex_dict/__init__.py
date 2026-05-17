#!/usr/bin/env python3

"""Dictionary utilities (DotDict, safe_merge) for the SciTeX ecosystem."""

from __future__ import annotations

# `importlib.metadata` is stdlib on every supported Python (>=3.10),
# so the only branch we still need is the editable / not-installed
# fallback that surfaces a clearly-fake version. No optional-import
# helper is needed here (this is stdlib, not a `[all]` dep).
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _v

try:
    __version__ = _v("scitex-dict")
except PackageNotFoundError:
    __version__ = "0.0.0+local"
del _v, PackageNotFoundError

from ._DotDict import DotDict
from ._flatten import flatten
from ._listed_dict import listed_dict
from ._pop_keys import pop_keys
from ._replace import replace
from ._safe_merge import safe_merge
from ._to_str import to_str

__all__ = [
    "__version__",
    "DotDict",
    "listed_dict",
    "pop_keys",
    "replace",
    "safe_merge",
    "to_str",
    "flatten",
]
