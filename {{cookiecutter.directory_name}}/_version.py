def _get_version() -> str:
    from pathlib import Path

    import versioningit

    import {{cookiecutter.package_name}}

    {{cookiecutter.package_name}}_path = Path({{cookiecutter.package_name}}.__file__).parent
    return versioningit.get_version(project_dir={{cookiecutter.package_name}}_path.parent)


__version__ = _get_version()
