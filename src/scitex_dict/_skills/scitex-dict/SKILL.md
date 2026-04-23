---
name: scitex-dict
description: Dict utilities for SciTeX — DotDict attribute access, safe merge, flatten, listed-dict, key popping, and string rendering. Use when working with config-like mappings.
user-invocable: false
---

# scitex-dict

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
