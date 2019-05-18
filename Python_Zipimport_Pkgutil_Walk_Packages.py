# Python zipimport — Import modules from Zip archives.
# This module adds the ability to import Python modules (*.py, *.pyc) and packages from ZIP-format archives.
# It is usually not needed to use the zipimport module explicitly; it is automatically used by the built-in
# import mechanism for sys.path items that are paths to ZIP archives.
# Typically, sys.path is a list of directory names as strings. This module also allows an item of sys.path to
# be a string naming a ZIP file archive. The ZIP archive can contain a subdirectory structure to support package
# imports, and a path within the archive can be specified to only import from a subdirectory.
# pkgutil.walk_packages(path=None, prefix='', onerror=None). 
# Yields ModuleInfo for all modules recursively on path, or, if path is None, all accessible modules.
# 'path' should be either None or a list of paths to look for modules in.
# 'prefix' is a string to output on the front of every module name on output.
# Note that this function must import all packages (not all modules!) on the given path, in order to access the
# __path__ attribute to find submodules.
# 'onerror' is a function which gets called with one argument (the name of the package which was being imported)
# if any exception occurs while trying to import a package. If no onerror function is supplied, ImportErrors are
# caught and ignored, while all other exceptions are propagated, terminating the search.
 
# list all modules python can access

walk_packages()

# list all submodules of ctypes

walk_packages(ctypes.__path__, ctypes.__name__ + '.')
