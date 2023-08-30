# Cookie Cutter Template

This is a cookicutter template for easy creation of a python package.

## Install cookiecutter

The first step is to make a new environment and install the cookiecutter package.
Launch a prompt and type:

```console
conda create -n cookiecutter python=3.10
conda activate cookiecutter
pip install cookiecutter
```

Alternative you can consult the [installation guide](https://cookiecutter.readthedocs.io/en/stable/installation.html).

## How to use this  cookie cutter template

The first step is to activate the cookiecutter environment, and execute the cookiecutter command:

```console
conda activate cookiecutter
cookiecutter.exe osprojecttemplate
```

You will be asked to enter some information about your project. After that the project will be created.
Note that the project will be created in the current directory.
Further, note that the last two questions are a workaround to get the project to work with GitHub actions. So just press enter to accept the default answers.

Second you need to make a Repo on GitHub and push the project to it.
To push the project to GitHub,
go to the new directory and execute:

```console
git init
git add .
git commit -m 'first commit'
git tag -a v0.0.0 -m "first tag"
git remote add origin https://github.com/<your githubpage>/<Repo Name>.git
git branch -M main
git push
git checkout -b gh-pages
git push --set-upstream origin gh-pages
git checkout main
```

### Set Up IO

go to: 
https://github.com/<your githubpage>/<Repo Name>/settings
and select the branch "gh-pages" and dir "root" 

Change these settings under Settings-Action-General. 
Workflow Permissions: Rean and Write
Allow GitHub Actions to approve pull requests
I'm not sure if both are needed, but enabling both got me past this
