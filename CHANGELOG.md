# Changelog

All notable changes to this fork of **requests-html** are recorded here.

## [0.10.1] – 2026-06-27

### Maintenance (this fork: pittmanbrandon20-design/requests-html)

This is a follow-up maintenance release building on the modernisation work in
`0.10.0` (see below). No public API changes.

#### CI / visibility
- Added a dedicated `render` CI job that runs the browser/Chromium test suite
  separately from the stable unit-test matrix.  The job is allowed to fail
  while the render backend (`pyppeteer`) is being stabilised, but it will now
  surface failures instead of hiding them.

#### Bug fixes / behaviour clarification
- `_convert_cookiejar_to_render`: falsy but meaningful cookie attributes
  (e.g. `secure=False`, `expires=0`) are now explicitly preserved.  Only
  `None` values (absent optional attributes) are omitted.  This corrects a
  regression introduced when the original `eval`-based implementation was
  replaced; that code used `if not v` which silently dropped `False` and `0`.

#### Tests
- Added focused edge-case tests for `_convert_cookiejar_to_render` covering
  `None` optional attributes, `secure=False`, and `expires=0`.
- Added a focused test for custom `browser_args` to verify they are passed
  through correctly.

#### Metadata
- Updated project URLs in `pyproject.toml` to point to this fork.
- Added `pytest-timeout` to dev dependencies (used by the render CI job).

---

## [0.10.0] – 2026-06-27

### Breaking changes

> **Python < 3.10 is no longer supported.**
>
> If you are running Python 3.6, 3.7, 3.8, or 3.9 you must either upgrade
> Python or pin `requests-html<0.10.0`.

### Modernisation (this fork: pittmanbrandon20-design/requests-html)

- **CI**: replaced Travis CI with GitHub Actions; Python matrix is now
  3.10 – 3.13.
- **Packaging**: migrated to `pyproject.toml` / PEP 517 build backend;
  removed legacy `UploadCommand` from `setup.py`.
- **Dependencies**: cleaned up `Pipfile`; replaced `white` with `black`;
  normalised PyPI index URL.
- **Runtime fixes**:
  - Removed unsafe `eval()` from cookie conversion; replaced with `getattr`.
  - Fixed mutable default argument for `browser_args` (`list` → `None`).
  - Modernised Python version guard (assert → explicit comparison).
  - Improved asyncio event-loop handling in `AsyncHTMLSession`.
- **README**: updated CI badge, install instructions, and Python support note.

---

*This project is a maintained fork of
[psf/requests-html](https://github.com/psf/requests-html), originally
authored by Kenneth Reitz.*
