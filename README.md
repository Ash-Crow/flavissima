# Django template

Django template, allowing to create a new site based on my favourite Django initial configuration, using the [twelve-factor methodology](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology).

A few details:

- The project is always called `config`. This helps locating the settings file when navigating between various Django websites, see [this article](https://dev.to/alansomathew/django-project-structure-best-practices-a-production-ready-guide-3io3) for the reasoning ;
- Dependencies are managed through [uv](https://docs.astral.sh/uv/) ;
- Commands are managed through [just](https://just.systems/man/en/).
- Pre-commit hooks control various aspects of the quality of the code. In particular:
  - [black](https://pypi.org/project/black/) and [ruff](https://docs.astral.sh/ruff/) are used for linting Python code
  - [djLint](https://djlint.com/) is used for linting HTML code
  - [bandit](https://pypi.org/project/bandit/) is used to check for security issues
  - [deptry](https://deptry.com/) is used to check for dependency issues
- Config settings are defined through environment variables.
