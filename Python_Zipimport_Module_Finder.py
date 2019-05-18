# Python zipimport — Import modules from Zip archives.
# This module adds the ability to import Python modules (*.py, *.pyc) and packages from ZIP-format archives.
# It is usually not needed to use the zipimport module explicitly; it is automatically used by the built-in
# import mechanism for sys.path items that are paths to ZIP archives.
# Typically, sys.path is a list of directory names as strings. This module also allows an item of sys.path to
# be a string naming a ZIP file archive. The ZIP archive can contain a subdirectory structure to support package
# imports, and a path within the archive can be specified to only import from a subdirectory.
# modulefinder — Find modules used by a script.
# Usage of ModuleFinder
 
import re, itertools

try:
    import baconhameggs

except ImportError:
    pass

try:
    import guido.python.ham

except ImportError:
    pass
