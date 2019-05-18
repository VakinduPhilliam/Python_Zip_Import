# Python zipimport — Import modules from Zip archives.
# This module adds the ability to import Python modules (*.py, *.pyc) and packages from ZIP-format archives.
# It is usually not needed to use the zipimport module explicitly; it is automatically used by the built-in
# import mechanism for sys.path items that are paths to ZIP archives.
# Typically, sys.path is a list of directory names as strings. This module also allows an item of sys.path to
# be a string naming a ZIP file archive. The ZIP archive can contain a subdirectory structure to support package
# imports, and a path within the archive can be specified to only import from a subdirectory.
# pkgutil.extend_path(path, name) 
# Extend the search path for the modules which comprise a package. Intended use is to place the following code
# in a package’s __init__.py:
 
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
