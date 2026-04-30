---
name: python-api
description: scitex-dict — Python API — see file body for details.
tags: [scitex-dict, scitex-package]
---

<!-- 02_python-api.md -->

# scitex-dict — Python API

From `scitex_dict.__all__`:

| Symbol | Kind | One-liner |
|--------|------|-----------|
| `DotDict` | class | `dict` subclass exposing keys as attributes, recursively. |
| `safe_merge` | function | Merge multiple dicts; raise on duplicate keys. |
| `flatten` | function | Collapse nested dicts into dotted single-level keys. |
| `listed_dict` | function | Create a `defaultdict(list)`-style helper dict. |
| `pop_keys` | function | Pop multiple keys from a dict in one call. |
| `replace` | function | Substitute values in a dict by a mapping. |
| `to_str` | function | Render a dict as a readable string. |

## Signatures (call shape only; see docstrings for full options)

```python
DotDict(data: dict | None = None)
safe_merge(*dicts: dict) -> dict
flatten(d: dict, sep: str = ".") -> dict
listed_dict(keys: Iterable | None = None) -> defaultdict
pop_keys(d: dict, keys: Iterable[str]) -> dict
replace(d: dict, mapping: dict) -> dict
to_str(d: dict) -> str
```

All helpers live under `scitex_dict/_*.py` (one file per symbol); open the
source for exact argument semantics.
