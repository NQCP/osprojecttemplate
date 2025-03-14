# Cookie Cutter Template
<p align="center">
  <img src="https://img.shields.io/static/v1?style=for-the-badge&label=code-status&message=Good&color=green"/>
  <img src="https://img.shields.io/static/v1?style=for-the-badge&label=initial-commit&message=RasmusBC59&color=inactive"/>
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=maintainer&message=NQCP&color=inactive"/>
</p>

This is a cookicutter template for easy creation of a python package.

## Install cookiecutter

The **first step** is to make a new environment and install the cookiecutter package.
Launch a prompt and type:

```console
conda create -n cookiecutter python=3.10
conda activate cookiecutter
pip install cookiecutter
```

Alternative you can consult the [installation guide](https://cookiecutter.readthedocs.io/en/stable/installation.html).

## How to use this  cookie cutter template

The **second** step is to activate the cookiecutter environment, and execute the cookiecutter command:

```console
conda activate cookiecutter
cookiecutter.exe https://github.com/NQCP/osprojecttemplate.git
```

You will be asked to enter some information about your project. After that the project will be created.

- directory_name: The name of the directory. This will be the name of the future repository and the folder contaning documentation, configuration files and a subfolder (package_name) containing the python files. Follow the naming convention in the [devops wiki](https://dev.azure.com/NQCP/NQCP/_wiki/wikis/NQCP.wiki/118/Code-repositories?anchor=standards-for-all-nqcp-code-repositories) (for example NQCP-Phot-Git-Drivers).
- package_name: The name of the package. This will be the name of the subfolder and the name of the package. Only use lower case letters.
- package_description: A short description of the package.
- author: Your name or the name of the author of the package.
- author_email: Your email address.
- copyrigh: Your name or the name of the orginasation which have the copyright to the package.
- a_start: a workaround to get the project to work with GitHub actions. So just press enter to accept the default answers.
- a_end: a workaround to get the project to work with GitHub actions. So just press enter to accept the default answers.

Note that the project will be created in the current directory.

The **third** step is to make a Repo, on GitHub or Azure DevOps. Thus, go to GitHub or Azure DevOps and create a new repository. Use the same directory_name from above as the repository name. Creating the repository will give you an URL, which you will need in the steps below. 

The **fourth** step is to push the project to GitHub or Azure DevOps. In the terminal, navigate to the project directory created earlier and execute:

```console
cd <directory_name>
git init
git add .
git commit -m "first commit"
git config --local core.hooksPath .githooks/
git tag -a v0.0.0 -m "first tag"
git remote add origin  <URL to your repo\>
git branch -M main
git push  --set-upstream origin main
git push  --tags
git checkout -b gh-pages
git push --set-upstream origin gh-pages
git checkout main
```

### Set Up IO
#### GitHub
If you are using GitHub, you can set up GitHub Pages to host the documentation.
go to: 
https://github.com/"your githubpage"/"Repo Name"/settings
and select the branch "gh-pages" and dir "root" 

Change these settings under Settings-Action-General. 
Workflow Permissions: Read and Write
Allow GitHub Actions to approve pull requests
I'm not sure if both are needed, but enabling both got me past this

#### Azure DevOps
TBW
