# {{cookiecutter.package_name}}

# Description

# Installation

# Usage

## Running the tests

If you have gotten '{{cookiecutter.package_name}}' from source, you may run the tests locally.

Install `{{cookiecutter.package_name}}` along with its test dependencies into your virtual environment by executing the following in the root folder

```bash
$ pip install .[test]
```

Then run `pytest` in the `tests` folder.

## Building the documentation

If you have gotten `{{cookiecutter.package_name}}` from source, you may build the docs locally.

Install `{{cookiecutter.package_name}}` along with its documentation dependencies into your virtual environment by executing the following in the root folder

```bash
$ pip install .[docs]
```

You also need to install `pandoc`. If you are using `conda`, that can be achieved by

```bash
$ conda install pandoc
```
else, see [here](https://pandoc.org/installing.html) for pandoc's installation instructions.

Then run `make html` in the `docs` folder. The next time you build the documentation, remember to run `make clean` before you run `make html`.
