'''
Text search and manipulation functions.
'''

import fnmatch

def disambiguate(pref, names):
    '''
    Return a list of disambiguated names from a prefix.
    '''

    return [name for name in names if name.startswith(pref)]

def glob(name, glob):
    '''
    Return True if a name string matches a glob pattern.
    '''

    return fnmatch.fnmatch(name, glob)
