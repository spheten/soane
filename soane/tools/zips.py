'''
Zipfile manipulation functions.
'''

import zipfile

from soane import tools

ZIP_OPTS = {
    'compression':   zipfile.ZIP_DEFLATED,
    'compresslevel': 5,
}

def create(path, addr, body):
    '''
    Write a new address to a zipfile.
    '''

    if exists(path, addr):
        raise FileExistsError(f'{addr!r} already exists in zip {path!r}')

    with zipfile.ZipFile(path, 'a', **ZIP_OPTS) as zobj:
        body = body.strip() + '\n'
        zobj.writestr(addr, body.encode('utf-8'))

def exists(path, addr):
    '''
    Return True if a zipfile contains an address.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        try:
            zobj.getinfo(addr)
            return True
        except KeyError:
            return False

def list_addrs(path):
    '''
    Return a list of all addresses in a zipfile.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        return zobj.namelist()

def list_infos(path):
    '''
    Return a list of all ZipInfo objects in a zipfile.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        return zobj.infolist()

def read(path, addr):
    '''
    Return the contents of an address from a zipfile.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        with zobj.open(addr, 'r') as fobj:
            return fobj.read().decode('utf-8')

def read_dict(path):
    '''
    Return an entire zipfile as an address-to-body dict.
    '''

    with zipfile.ZipFile(path, 'r', **ZIP_OPTS) as zobj:
        zdict = {}
        for addr in zobj.namelist():
            with zobj.open(addr, 'r') as fobj:
                zdict[addr] = fobj.read().decode('utf-8')
        return zdict

def update(path, addr, body):
    '''
    Overwrite an existing address in a zipfile.
    '''

    if not exists(path, addr):
        raise FileNotFoundError(f'{addr!r} does not exist in zip {path!r}')

    zdict = read_dict(path)
    zdict[addr] = body

    with zipfile.ZipFile(path, 'w', **ZIP_OPTS) as zobj:
        for addr, body in zdict.items():
            body = body.strip() + '\n'
            zobj.writestr(addr, body.encode('utf-8'))

def write_dict(path, zdict):
    '''
    Overwrite an entire zipfile with an address-to-body dict.
    '''

    with zipfile.ZipFile(path, 'w', **ZIP_OPTS) as zobj:
        for addr, body in zdict.items():
            body = body.strip() + '\n'
            zobj.writestr(addr, body.encode('utf-8'))
