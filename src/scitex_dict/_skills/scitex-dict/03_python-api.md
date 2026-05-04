---
description: |
  [TOPIC] scitex-dict Python API
  [DETAILS] All 7 public callables — DotDict, safe_merge, flatten, listed_dict, pop_keys, replace, to_str.
tags: [scitex-dict-python-api]
---

# Python API

## Imports

```python
from scitex_dict import (
    DotDict,
    safe_merge,
    flatten,
    listed_dict,
    pop_keys,
    replace,
    to_str,
)
```

## `DotDict`

Subclass of `dict` that supports attribute access. Recursive — nested
dict values are wrapped automatically.

```python
d = DotDict({"a": {"b": 1}})
d.a.b               # 1
d.a.b = 2           # mutation works through attribute
"a" in d            # True (still behaves like a dict)
```

## `safe_merge(*dicts) -> dict`

Merge multiple dicts. Raises `ValueError` on overlapping keys. Use
when conflicts indicate a bug rather than a deliberate override.

## `flatten(d, sep=".") -> dict`

Recursively flatten a nested dict into a single level. Keys joined by
`sep`. Reverse via custom unflatten if needed.

## `listed_dict(items) -> dict[K, list[V]]`

Build a `defaultdict(list)`-style dict from `(key, value)` pairs.

```python
listed_dict([("a", 1), ("a", 2), ("b", 3)])
# {"a": [1, 2], "b": [3]}
```

## `pop_keys(d, keys) -> list`

In-place: pop multiple keys at once and return their values.

## `replace(d, mapping) -> dict`

Walk a dict (and nested dicts/lists) and substitute string fragments
according to `mapping`. Useful for templated configs.

## `to_str(d, indent=2) -> str`

Pretty-print a dict. Uses ASCII-friendly formatting suitable for log
output.

## Two import paths

```python
import scitex_dict        # standalone
import scitex.dict        # umbrella (requires `pip install scitex`)
```
