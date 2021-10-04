'''
File path manipulation functions.
'''

import os.path
import string

SLUG_CHARS = string.ascii_lowercase + string.digits + '-_'
EXPANDERS  = {
    '~': os.path.expanduser,
    '%': os.path.expandvars,
    '$': os.path.expandvars,
}

def base(path):
    '''
    Return a path's base name, with its extension.
    '''

    return os.path.basename(path)

def clean(path):
    '''
    Return a clean normalised path.
    '''

    return os.path.normpath(str(path))

def dire(path):
    '''
    Return a path's parent directory.
    '''

    return os.path.dirname(path)

def expand(path):
    '''
    Return a clean token-expanded path.
    '''

    for char, func in EXPANDERS.items():
        if char in path:
            path = func(path)
    return os.path.normpath(path)

def exists(path):
    '''
    Return True if a path exists on disk.
    '''

    return os.path.isfile(path)

def ext(path):
    '''
    Return a path's extension, without the dot.
    '''

    return os.path.splitext(path)[1].lstrip('.')

def join(*elems):
    '''
    Return a clean joined path.
    '''

    path = os.path.join(*map(str, elems))
    return os.path.normpath(path)

def name(path):
    '''
    Return a path's base name, without its extension.
    '''

    base = os.path.basename(path)
    return os.path.splitext(base)[0]
