# scitex-dict

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Dictionary utilities — DotDict, safe_merge, flatten, listed_dict, replace.</b></p>

<p align="center">
  <a href="https://scitex-dict.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-dict</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-dict/"><img src="https://img.shields.io/pypi/v/scitex-dict.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/scitex-dict/"><img src="https://img.shields.io/pypi/pyversions/scitex-dict.svg" alt="Python"></a>
  <a href="https://github.com/ywatanabe1989/scitex-dict/actions/workflows/test.yml"><img src="https://github.com/ywatanabe1989/scitex-dict/actions/workflows/test.yml/badge.svg" alt="Tests"></a>
  <a href="https://github.com/ywatanabe1989/scitex-dict/actions/workflows/install-test.yml"><img src="https://github.com/ywatanabe1989/scitex-dict/actions/workflows/install-test.yml/badge.svg" alt="Install Test"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-dict"><img src="https://codecov.io/gh/ywatanabe1989/scitex-dict/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scitex-dict.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/scitex-dict/badge/?version=latest" alt="Docs"></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/license-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **YAML config access ergonomics** — `CONFIG["MODEL"]["hidden_size"]` vs `CONFIG.MODEL.hidden_size` matters in a notebook | **`DotDict`** — attribute-access `dict` subclass with recursive `.x.y.z`; works as a drop-in for the umpteen competing alternatives (addict, easydict, box, dotmap) |
| 2 | **Merging configs silently overwrites** — `{**a, **b}` on duplicate keys loses information | **`safe_merge`** — duplicate keys raise; `flatten` turns nested dicts into dotted-key single-level for logging/CSV |

## Installation

```bash
pip install scitex-dict
```

## Architecture

```
scitex-dict/
├── src/scitex_dict/
│   ├── _DotDict.py        # attribute-access dict subclass
│   ├── _safe_merge.py     # raises on duplicate keys
│   ├── _flatten.py        # nested → dotted-key
│   └── _listed_dict.py    # default-list dict factory
└── tests/
```

## 1 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
from scitex_dict import (
    DotDict, flatten, listed_dict, pop_keys,
    replace, safe_merge, to_str,
)

cfg = DotDict({"model": {"lr": 0.001}})
cfg.model.lr                              # 0.001

safe_merge({"a": 1}, {"b": 2})

flatten({"x": {"y": 1, "z": [10, 20]}})   # {"x_y": 1, "x_z_0": 10, ...}

d = listed_dict(["a", "b"])

replace("hello world", {"hello": "hi"})   # "hi world"

to_str({"a": 1, "b": 2})
```

</details>

## Demo

```mermaid
flowchart LR
    YAML[YAML config] --> DD[DotDict]
    DD -->|cfg.model.lr| Code[Your code]
    A[dict A] --> SM[safe_merge]
    B[dict B] --> SM
    SM --> Merged[merged dict]
```

## Quick Start

```python
from scitex_dict import DotDict, safe_merge

cfg = DotDict({"model": {"lr": 0.001, "epochs": 100}})
print(cfg.model.lr)              # 0.001

merged = safe_merge({"a": 1}, {"b": 2})
```

## Part of SciTeX

`scitex-dict` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[dict]` to use as
`scitex.dict` (Python) or `scitex dict ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0. See [LICENSE](LICENSE).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
