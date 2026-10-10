# Flavissima

![Logo](flavissima/static/flavissima/img/logo.svg)

Flavissima aims at creating a [Wagtail](https://wagtail.org/)-based CMS with components based on [DaisyUI](https://daisyui.com/).

## Requirements

- [uv](https://docs.astral.sh/uv/) >= 0.9.17
- [npm](https://www.npmjs.com/) >= 11.10.0
- [just](https://just.systems/) >= 1.27.0

As a supply-chain safety measure, uv and npm only install package versions released at least 7 days ago (see `exclude-newer` in `pyproject.toml` and `min-release-age` in `.npmrc`), and `just upgrade` only bumps pre-commit hooks to releases at least 7 days old (via `prek update --cooldown-days 7`).
