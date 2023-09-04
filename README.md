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
cookiecutter.exe https://github.com/NQCP/osprojecttemplate.git
```

You will be asked to enter some information about your project. After that the project will be created.

- directory_name: The name of the directory. This will be the name of the folder contaning documentation, configuration files and a subfolder (package_name) containing the python files. Use CamelCase.
- package_name: The name of the package. This will be the name of the folder and the name of the package. Remember to only use small letters.
- package_description: A short description of the package.
- author: Your name or the name of the author of the package.
- author_email: Your email address.
- copyrigh: Your name or the name of the orginasation which have the copyright to the package.
- a_start: a workaround to get the project to work with GitHub actions. So just press enter to accept the default answers.
- a_end: a workaround to get the project to work with GitHub actions. So just press enter to accept the default answers.

Note that the project will be created in the current directory.

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
git push  --set-upstream origin main
git push  --tags
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
