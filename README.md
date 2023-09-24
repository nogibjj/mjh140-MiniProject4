# Mini Project 4: Matrix Testing

### Github Actions:
[![Python Version: 3.8, 3.9, 3.11](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/python_matrix.yml/badge.svg)](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/python_matrix.yml)   [![Install](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/install.yml)   [![Format](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/format.yml)   [![Linting](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/lint.yml)   [![Unit Tests](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/unitTests.yml/badge.svg)](https://github.com/nogibjj/mjh140-MiniProject4/actions/workflows/unitTests.yml)
***
### Objective: 
Setup GitHub Actions matrix testing for multiple python versions
***
### Matrix Implementation:
The matrix testing was implemented in the `.github/workflows/python_matrix.yml` YAML file. A snapshot of the YAML file is shown below. Matrix testing was implemented as a build strategy. In addition to python version, OS system was also included under the "matrix" subsection of "strategy" in case different OS systems need to be tested. Only Ubuntu was used for this project. Python versions 3.8, 3.9, and 3.11 were all verified. 

```python
name: "Python Version: 3.8, 3.9, 3.11  "
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ] 
  workflow_dispatch:
jobs:
  build:
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.11]
        os: [ubuntu-latest]
    runs-on: ${{matrix.os}}
    steps:
      - uses: actions/checkout@v3
      - name: venv activation
        run: |
          make venv
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v1
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install
        run: |
          make install
      - name: Format
        run: |
          make format
      - name: Pylint
        run: |
          make lint
      - name: Unit Tests
        run: |
          make test
```

The rest of this repository implements a basic main.py and test_1.py file within the `/src` and `/tests` directories respectively.
