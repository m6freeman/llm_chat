
# Python Project Template

A simple, /src/ structured, declaritively set up, template for Python Projects.

### HOW TO USE THIS TEMPLATE

> **DO NOT FORK**  **[Use the template](https://github.com/m6freeman/python_project_template/generate)** 

### What is included on this template?

```bash
├── .gitignore               # A list of files to ignore when pushing to Github
├── conftest.py              # File to instruct pytest where project root is 
├── docs                     # Documentation site (add more .md files here)
│   └── index.md             # The index page for the docs site
├── pyproject.toml           # Declare project build architecture
├── README.md                # The main readme for the project
├── requirements.txt         # Base packaging, testing, formatting modules. Includes result module for Rust-like Result syntax
├── setup.cfg                # Project installing and packaging configurations
├── src                      # Parent directory for all packages
│   └── my_package           # Package level directory
│       ├── __init__.py      # Initialization file for package
│       ├── my_module.py     # Template module file
└── tests                    # Parent directory for all tests
    ├── __main__.py          # Required by pytest
    └── test_my_package.py   # Test file for my_package
```

---
# project_name

[![codecov](https://codecov.io/gh/author_name/project_urlname/branch/main/graph/badge.svg?token=project_urlname_token_here)](https://codecov.io/gh/author_name/project_urlname)
[![CI](https://github.com/author_name/project_urlname/actions/workflows/main.yml/badge.svg)](https://github.com/author_name/project_urlname/actions/workflows/main.yml)

project_description

## Install it from PyPI

```bash
pip install project_name
```

## Usage

```py
from project_name import BaseClass
from project_name import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m project_name
#or
$ project_name
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
