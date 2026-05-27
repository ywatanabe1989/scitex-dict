---
description: |
  [TOPIC] scitex-dict Installation
  [DETAILS] pip install scitex-dict (pure Python, requires scitex-dev>=0.11.7 for entry-point registration); smoke verify with import + DotDict.
tags: [scitex-dict-installation]
---

# Installation

## Standard

```bash
pip install scitex-dict
```

Pure-Python (stdlib-only); requires ``scitex-dev>=0.11.7`` for Skills / Docs entry-point
registration (the ``[all]`` extra is empty — no graceful-degradation deps exist).

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
