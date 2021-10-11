'''
File input/output and manipulation functions.
'''

import glob as glob_
import os
import shutil

import send2trash

from soane import tools

FILE_OPTS = {
    'encoding': 'utf-8',
}

def copy(path, name):
    '''
    Copy a file to another name in the same directory and return
    the new path.
    '''

    dire = tools.path.dire(path)
    ext  = tools.path.ext(path)
    dest = tools.path.join(dire, f'{name}.{ext}')
    shutil.copyfile(path, dest)
    return dest

def create(path, body):
    '''
    Create a new file containing a string.
    '''

    with open(path, 'x', **FILE_OPTS) as fobj:
        fobj.write(body.strip() + '\n')

def delete(path):
    '''
    Delete a file by sending it to system trash.
    '''

    send2trash.send2trash(path)

def exists(path, dire=False):
    '''
    Return True if a file or directory exists.
    '''

    if dire:
        return os.path.isdir(path)
    else:
        return os.path.isfile(path)

def glob(dire, term):
    '''
    Yield all files in a directory matching a glob pattern.
    '''

    path = tools.path.join(dire, term)
    yield from glob_.iglob(path)

def read(path):
    '''
    Return the contents of an existing file as a string.
    '''

    with open(path, 'r', **FILE_OPTS) as fobj:
        return fobj.read().strip() + '\n'

def move(path, name):
    '''
    Move a file to another name in the same directory and return the new path.
    '''

    dire = tools.path.dire(path)
    ext  = tools.path.ext(path)
    dest = tools.path.join(dire, f'{name}.{ext}')
    shutil.move(path, dest)
    return dest

def write(path, body):
    '''
    Write a string to a new or existing file.
    '''

    with open(path, 'w', **FILE_OPTS) as fobj:
        fobj.write(body.strip() + '\n')
