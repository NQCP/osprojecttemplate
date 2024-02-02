# {{cookiecutter.package_name}}
<p align="center">
  <img src="https://img.shields.io/static/v1?style=for-the-badge&label=code-status&message=Good&color=green"/>
  <img src="https://img.shields.io/static/v1?style=for-the-badge&label=initial-commit&message={{cookiecutter.author}}&color=inactive"/>
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=maintainer&message={{cookiecutter.copyright}}&color=inactive"/>
</p>

## Repo quality
We employ a rough 'stoplight' system for signifying the quality of code in a any given repo. Whenever you make a new repo, add any of the following badges to the top of your `README.md` file. Below is (rough) definitions of stoplight system currently in use. Use your own best judgement for your code :-)

<img src="https://img.shields.io/static/v1?style=flat-square&label=code-status&message=Caution!&color=red" style=“vertical-align:middle;”/> Here be dragons. This could be code straight from an experiment with no guarantees for its portability. Expect a collection of scripts and just barely `docstrings`
  
<img src="https://img.shields.io/static/v1?style=flat-square&label=code-status&message=Good&color=green"/> Decently factored code with well-documented and somewhat portable programming.
  
<img src="https://img.shields.io/static/v1?style=flat-square&label=code-status&message=Great!&color=brightgreen"/> High-level fully featured code with many moving parts and used broadly.

These banners generated from <a href=https://shields.io/>shields.io</a>.

# Description
[Examples](https://nqcp.github.io/{{cookiecutter.directory_name}}/example_notebooks/index.html)
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
