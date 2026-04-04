# scitex-dict

Dictionary utilities for the SciTeX ecosystem.

## Features

- **DotDict** -- Dot-access dictionary with recursive nesting, JSON serialization, and full `dict` protocol
- **safe_merge** -- Merge multiple dicts with overlap detection
- **flatten** -- Flatten nested dicts into single-level with separator keys
- **listed_dict** -- `defaultdict(list)` factory with optional pre-initialized keys
- **pop_keys** -- Remove specified keys from a key list
- **replace** -- Bulk string replacement using a mapping dict
- **to_str** -- Convert a dict to a compact string representation

## Installation

```bash
pip install scitex-dict
```

## Usage

```python
from scitex_dict import DotDict, safe_merge

cfg = DotDict({"model": {"lr": 0.001, "epochs": 100}})
print(cfg.model.lr)  # 0.001

merged = safe_merge({"a": 1}, {"b": 2})
# {"a": 1, "b": 2}
```

## License

AGPL-3.0. See [LICENSE](LICENSE).
