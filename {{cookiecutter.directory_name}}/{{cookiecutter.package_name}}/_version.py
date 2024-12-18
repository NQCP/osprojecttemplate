def _get_version() -> str:
    from pathlib import Path
    import versioningit
    import {{cookiecutter.package_name}}

    path = Path({{cookiecutter.package_name}}.__file__).parent
    project_dir = path.parent

    # Check if running from site-packages and it indicates that the package has been installed
    if "site-packages" in str(project_dir):
        # Traverse up to find the root project directory
        for parent in Path(__file__).resolve().parents:
            if (parent / "pyproject.toml").exists():
                project_dir = parent
                break

    if not (project_dir / "pyproject.toml").exists():
        raise FileNotFoundError("pyproject.toml not found in the project directory")

    print(f"Project directory: {project_dir}")

    version = versioningit.get_version(project_dir=project_dir)
    print(f"Retrieved version: {version}")

    return version

__version__ = _get_version()
