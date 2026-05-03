---
name: scitex-dict
description: |
  [WHAT] Dictionary utilities — `DotDict` (attribute-access dict), `safe_merge` (raise-on-conflict), `flatten`, `listed_dict`, `pop_keys`, `replace`, `to_str`.
  [WHEN] Accessing config values with dot notation, merging dicts safely, flattening nested dicts for logging/CSV, popping multiple keys, recursive string substitution, or pretty-printing.
  [HOW] `from scitex_dict import DotDict, safe_merge, flatten, listed_dict, pop_keys, replace, to_str` — wrap a YAML/dict and use functional helpers.
tags: [scitex-dict]
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 1
  http: 0
---

# scitex-dict

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐ · Hook — · HTTP —

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
