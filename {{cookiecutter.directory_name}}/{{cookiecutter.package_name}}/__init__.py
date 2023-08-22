import logging
import {{cookiecutter.package_name}}._version


__version__ = {{cookiecutter.package_name}}._version.__version__



logger = logging.getLogger(__name__)
logger.info(f'Imported {{cookiecutter.package_name}}version: {__version__}')
