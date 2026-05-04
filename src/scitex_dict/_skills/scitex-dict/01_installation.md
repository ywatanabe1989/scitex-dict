---
description: |
  [TOPIC] scitex-dict Installation
  [DETAILS] pip install scitex-dict (pure Python, no required deps); smoke verify with import + DotDict.
tags: [scitex-dict-installation]
---

# Installation

## Standard

```bash
pip install scitex-dict
```

Pure-Python; no required runtime dependencies.

## Verify

```bash
python -c "import scitex_dict; print(scitex_dict.__version__)"
python -c "from scitex_dict import DotDict, safe_merge, flatten; print('ok')"
```

## Editable install (development)

```bash
git clone https://github.com/ywatanabe1989/scitex-dict
cd scitex-dict
pip install -e '.[dev]'
```

## Umbrella alternative

```bash
pip install scitex   # exposes scitex.dict as a submodule
```

See SKILL.md for the standalone-vs-umbrella import rule.
