---
description: |
  [TOPIC] scitex-dict Quick start
  [DETAILS] DotDict attribute access, safe_merge raise-on-conflict, flatten for logging/CSV.
tags: [scitex-dict-quick-start]
---

# Quick Start

## DotDict — attribute access over dict

```python
from scitex_dict import DotDict

cfg = DotDict({"db": {"url": "sqlite://", "pool": 4}})
print(cfg.db.url)            # "sqlite://"
cfg.db.pool = 8              # mutate via attribute
```

`DotDict` recurses into nested dicts — `cfg.db` is itself a `DotDict`.

## safe_merge — raise on conflict

```python
from scitex_dict import safe_merge

merged = safe_merge({"a": 1}, {"b": 2})         # {"a": 1, "b": 2}
safe_merge({"a": 1}, {"a": 2})                  # raises ValueError
```

Use this when you want to combine two configs and *fail loudly* if they
disagree.

## flatten — nested dict → flat dict

```python
from scitex_dict import flatten

flatten({"a": {"b": {"c": 1}}})
# {"a.b.c": 1}
```

Handy for logging structured config to CSV / TensorBoard / wandb.

## pop_keys / replace / to_str

```python
from scitex_dict import pop_keys, replace, to_str

cfg = {"a": 1, "b": 2, "c": 3}
pop_keys(cfg, ["b", "c"])              # cfg is now {"a": 1}

replace({"msg": "hello $name"}, {"$name": "world"})
# {"msg": "hello world"}

to_str({"a": 1, "b": 2})               # pretty-printed multi-line string
```

## Next

- [03_python-api.md](03_python-api.md) — all 7 public symbols
- [SKILL.md](SKILL.md) — overview
