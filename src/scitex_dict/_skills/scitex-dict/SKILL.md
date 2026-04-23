---
name: scitex-dict
description: Dictionary utilities for scientific Python — attribute-access dicts, conflict-aware merging, nested flattening, and pretty rendering. Public API (7 symbols) — `DotDict` (attribute-access `dict` subclass with recursive `.x.y.z` lookup for YAML configs), `safe_merge(*dicts)` (merge with duplicate-key error instead of silent overwrite), `flatten(nested, sep=".")` (nested dict → single-level with dotted keys), `listed_dict(keys=None)` (`defaultdict(list)` factory), `pop_keys(d, keys)` (pop multiple keys at once, returning remaining dict), `replace(d, old, new)` (recursive string-substitution in keys and values), `to_str(d, delimiter=", ")` (human-readable rendering). No CLI, no MCP tools. Drop-in replacement for `SimpleNamespace`/`types.SimpleNamespace`, `addict.Dict`, `easydict.EasyDict`, `box.Box`, `dotmap.DotMap`, `collections.defaultdict(list)`, hand-rolled `{**a, **b}` merges that silently overwrite, and bespoke recursive-flatten/pretty-print helpers. Use whenever the user asks to "access config values with dot notation", "convert YAML into an attribute-accessible object", "merge two dicts but raise on conflict", "flatten a nested dict for logging/CSV", "pop several keys from a dict", "recursively substitute placeholder strings in a config", "pretty-print a dict", "use DotDict", or mentions scitex.dict, addict, easydict, dotted-key config.
user-invocable: false
primary_interface: python
---

# scitex-dict

> **Primary interface: Python API.** Import in scripts/notebooks — CLI & MCP are thin wrappers over the Python functions.

Lightweight dictionary helpers. The flagship type is `DotDict` (attribute
access over `dict`), alongside a handful of functional helpers.

## Installation & import (two equivalent paths)

The same module is reachable via two install paths. Both forms work at
runtime; which one a user has depends on their install choice.

```python
# Standalone — pip install scitex-dict
import scitex_dict
scitex_dict.DotDict(...)

# Umbrella — pip install scitex
import scitex.dict
scitex.dict.DotDict(...)
```

`pip install scitex-dict` alone does NOT expose the `scitex` namespace;
`import scitex.dict` raises `ModuleNotFoundError`. To use the
`scitex.dict` form, also `pip install scitex`.

See [../../general/02_interface-python-api.md] for the ecosystem-wide
rule and empirical verification table.

## Sub-skills

- [01_quick-start.md](01_quick-start.md) — install, import, common patterns
- [02_python-api.md](02_python-api.md) — all 7 public symbols

No CLI, no MCP tools.
