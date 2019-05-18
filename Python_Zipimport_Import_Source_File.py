# Python zipimport — Import modules from Zip archives.
# This module adds the ability to import Python modules (*.py, *.pyc) and packages from ZIP-format archives.
# It is usually not needed to use the zipimport module explicitly; it is automatically used by the built-in
# import mechanism for sys.path items that are paths to ZIP archives.
# Typically, sys.path is a list of directory names as strings. This module also allows an item of sys.path to
# be a string naming a ZIP file archive. The ZIP archive can contain a subdirectory structure to support package
# imports, and a path within the archive can be specified to only import from a subdirectory.
# importlib — The implementation of import.
# Importing a source file directly.
# To import a Python source file directly, use the following recipe (Python 3.5 and newer only):
 
import importlib.util
import sys

# For illustrative purposes.

import tokenize

file_path = tokenize.__file__
module_name = tokenize.__name__

spec = importlib.util.spec_from_file_location(module_name, file_path)

module = importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)

# Optional; only necessary if you want to be able to import the module
# by name later.

sys.modules[module_name] = module
