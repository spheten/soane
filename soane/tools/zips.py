'''
Zipfile manipulation functions.
'''

import zipfile

from soane import tools

ZIP_OPTS = {
    'compression':   zipfile.ZIP_DEFLATED,
    'compresslevel': 5,
}

def append(path, name, body):
    '''
    Write a new file to a zipfile.
    '''

    if exists(path, name):
        raise FileExistsError(f'{name!r} already exists in zip {path!r}')

    with zipfile.ZipFile(path, 'a', **ZIP_OPTS) as zobj:
        body = body.strip() + '\n'
        zobj.writestr(name, body.encode('utf-8'))

def exists(path, name):
    '''
    Return True if a zipfile contains a named file.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        try:
            zobj.getinfo(name)
            return True
        except KeyError:
            return False

def list_infos(path):
    '''
    Return a list of all ZipInfo objects in a zipfile.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        return zobj.infolist()

def list_names(path):
    '''
    Return a list of all file names in a zipfile.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        return zobj.namelist()

def read(path, name):
    '''
    Return the contents of a file from a zipfile.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        with zobj.open(name, 'r') as fobj:
            return fobj.read().decode('utf-8')

def read_all(path):
    '''
    Return an entire zipfile as a '{name: body}' dict.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        zdict = {}
        for name in zobj.namelist():
            with zobj.open(name, 'r') as fobj:
                zdict[name] = fobj.read().decode('utf-8')
        return zdict

def write(path, name, body):
    '''
    Overwrite a file in a zipfile with a string.
    '''

    if not exists(path, name):
        raise FileNotFoundError(f'{name!r} does not exist in zip {path!r}')

    zdict = read_all(path)
    zdict[name] = body

    with zipfile.ZipFile(path, 'w', **ZIP_OPTS) as zobj:
        for name, body in zdict.items():
            body = body.strip() + '\n'
            zobj.writestr(name, body.encode('utf-8'))

def write_all(path, zdict):
    '''
    Overwrite an entire zipfile with a '{name: body}' dict.
    '''

    with zipfile.ZipFile(path, 'w', **ZIP_OPTS) as zobj:
        for name, body in zdict.items():
            body = body.strip() + '\n'
            zobj.writestr(name, body.encode('utf-8'))
