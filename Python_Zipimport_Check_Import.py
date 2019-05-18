# Python zipimport — Import modules from Zip archives.
# This module adds the ability to import Python modules (*.py, *.pyc) and packages from ZIP-format archives.
# It is usually not needed to use the zipimport module explicitly; it is automatically used by the built-in
# import mechanism for sys.path items that are paths to ZIP archives.
# Typically, sys.path is a list of directory names as strings. This module also allows an item of sys.path to
# be a string naming a ZIP file archive. The ZIP archive can contain a subdirectory structure to support package
# imports, and a path within the archive can be specified to only import from a subdirectory.
# importlib — The implementation of import.
# Checking if a module can be imported.
# If you need to find out if a module can be imported without actually doing the import, then you should use
# importlib.util.find_spec().
 
import importlib.util
import sys

# For illustrative purposes.

name = 'itertools'

spec = importlib.util.find_spec(name)

if spec is None:

    print("can't find the itertools module")

else:

    # If you chose to perform the actual import ...

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Adding the module to sys.modules is optional.

    sys.modules[name] = module
