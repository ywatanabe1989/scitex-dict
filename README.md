# scitex-dict

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-dict.svg)](https://pypi.org/project/scitex-dict/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-dict.svg)](https://pypi.org/project/scitex-dict/)
[![Tests](https://github.com/ywatanabe1989/scitex-dict/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-dict/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-dict/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-dict/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-dict/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-dict)
[![Docs](https://readthedocs.org/projects/scitex-dict/badge/?version=latest)](https://scitex-dict.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->


Dictionary utilities for the SciTeX ecosystem.

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐ · Hook — · HTTP —

## Problem and Solution


| # | Problem | Solution |
|---|---------|----------|
| 1 | **YAML config access ergonomics** -- `CONFIG["MODEL"]["hidden_size"]` vs `CONFIG.MODEL.hidden_size` matters in a notebook | **`DotDict`** -- attribute-access `dict` subclass with recursive `.x.y.z`; works as a drop-in for the umpteen competing alternatives (addict, easydict, box, dotmap) |
| 2 | **Merging configs silently overwrites** -- `{**a, **b}` on duplicate keys loses information | **`safe_merge`** -- duplicate keys raise; `flatten` turns nested dicts into dotted-key single-level for logging/CSV |

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
