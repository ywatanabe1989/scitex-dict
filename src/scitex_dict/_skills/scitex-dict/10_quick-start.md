---
description: |
  [TOPIC] Quick Start
  [DETAILS] Install, import, and common DotDict / safe_merge / flatten patterns.
tags: [scitex-dict-quick-start]
---

<!-- 01_quick-start.md -->

# scitex-dict — Quick Start

## Install

```bash
pip install scitex-dict
```

## Import

```python
from scitex_dict import DotDict, safe_merge, flatten
```

## Usage

### DotDict — attribute access

```python
from scitex_dict import DotDict

cfg = DotDict({"lr": 1e-3, "model": {"layers": 4}})
cfg.lr                  # 1e-3
cfg.model.layers        # 4  (nested dicts are recursively wrapped)
cfg.new_key = "value"   # mutable
```

### safe_merge — non-destructive dict merge

```python
from scitex_dict import safe_merge

merged = safe_merge({"a": 1}, {"b": 2})   # {'a': 1, 'b': 2}
# Raises on conflicting keys rather than silently overwriting.
```

### flatten — collapse nested dicts

```python
from scitex_dict import flatten

flatten({"a": {"b": 1, "c": 2}})     # {'a.b': 1, 'a.c': 2}
```
