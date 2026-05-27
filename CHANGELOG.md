# Changelog

All notable changes to `scitex-dict` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.7] — 2026-05-09

- Fix CI: repair docs + quality workflows after upstream template changes.
- Tests: rewrite for PA-307 test-quality (TQ002/TQ003/TQ007).
- CI(codecov): disable PR comments (``comment: false``) to stop email noise.

## [0.1.6] — 2026-05-07

- Fix workflows: standardize to scitex-dev canonical set.
- Resync integrated release pipeline from scitex-dev v0.11.20.

## [0.1.5] — 2026-05-01

- **Deps**: adopt three-tier pyproject.toml policy; add ``scitex-dev>=0.11.7``
  as hard dependency for Skills / Docs entry-point registration.
- **Docs**: add CHANGELOG.md, Architecture + Demo sections, skill pages
  (installation/quick-start/python-api), canonical README structure per
  ecosystem audit (PS120/PS127/PS131/PS133/PS141/PS142/PS143).
- **CI**: add docs.yml, quality workflow, release pipeline, publish-pypi.yml,
  weekly doc-quality workflow.
- **Audit**: integrate audit-all into the test suite.

## [0.1.4] — 2026-04-30

- Add canonical ``__version__`` block via ``importlib.metadata``.
- PA501 + PA201 compliance: ``from __future__ import annotations``,
  ``__version__`` in ``__all__``.
- Add canonical skill frontmatter (name, description, tags) to all skill
  pages.
- Release-safety: opt-in publish-pypi.yml (``workflow_dispatch`` only).
- Audit-project compliance: tests mirror source layout.

## [0.1.3]

- Initial CHANGELOG entry — see git log for prior history.
