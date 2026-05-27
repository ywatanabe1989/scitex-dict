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

## `flatten(d, sep="_") -> dict`

Recursively flatten a nested dict into a single level. Keys joined by
``sep`` (default ``"_"``). Lists are indexed numerically. Reverse via
custom unflatten if needed.

## `listed_dict(items) -> dict[K, list[V]]`

Build a `defaultdict(list)`-style dict from `(key, value)` pairs.

```python
listed_dict([("a", 1), ("a", 2), ("b", 3)])
# {"a": [1, 2], "b": [3]}
```

## `pop_keys(items, keys) -> list`

Return a new list with any occurrences of the given keys removed.
Does not mutate the input collection.

## `replace(string, mapping) -> str`

Perform sequential string substitutions according to ``mapping``.
Useful for templated strings.

## `to_str(d, delimiter="_") -> str`

Render a dict as a ``delimiter``-separated string of ``key-value`` pairs.
Default delimiter is ``"_"``.

## Two import paths

```python
import scitex_dict        # standalone
import scitex.dict        # umbrella (requires `pip install scitex`)
```
