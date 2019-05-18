# Python zipimport — Import modules from Zip archives.
# This module adds the ability to import Python modules (*.py, *.pyc) and packages from ZIP-format archives.
# It is usually not needed to use the zipimport module explicitly; it is automatically used by the built-in
# import mechanism for sys.path items that are paths to ZIP archives.
# Typically, sys.path is a list of directory names as strings. This module also allows an item of sys.path to
# be a string naming a ZIP file archive. The ZIP archive can contain a subdirectory structure to support package
# imports, and a path within the archive can be specified to only import from a subdirectory.
# importlib — The implementation of import.
# Approximating importlib.import_module().
# Import itself is implemented in Python code, making it possible to expose most of the import machinery through
# importlib. 

import importlib.util
import sys

def import_module(name, package=None):
    """An approximate implementation of import."""

    absolute_name = importlib.util.resolve_name(name, package)

    try:
        return sys.modules[absolute_name]

    except KeyError:
        pass

    path = None

    if '.' in absolute_name:
        parent_name, _, child_name = absolute_name.rpartition('.')
        parent_module = import_module(parent_name)

        path = parent_module.__spec__.submodule_search_locations

    for finder in sys.meta_path:
        spec = finder.find_spec(absolute_name, path)

        if spec is not None:
            break

    else:
        raise ImportError(f'No module named {absolute_name!r}')

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)
    sys.modules[absolute_name] = module

    if path is not None:
        setattr(parent_module, child_name, module)

    return module
