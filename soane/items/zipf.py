'''
Class definition for 'ZipFile'.
'''

import contextlib
import zipfile

from soane import tools

class ZipFile:
    '''
    A plaintext zipfile container and controller.
    '''

    compression   = zipfile.ZIP_DEFLATED
    compresslevel = 5

    def __init__(self, path):
        '''
        Initialise a new Zipfile.
        '''

        self.path = tools.path.clean(path)

    def __contains__(self, addr):
        '''
        Return True if the Zipfile contains an address.
        '''

        with self.open('r') as zobj:
            try:
                zobj.getinfo(addr)
                return True
            except KeyError:
                return False

    def __eq__(self, zipf):
        '''
        Return True if the Zipfile is equal to another Zipfile.
        '''

        return all([
            isinstance(zipf, ZipFile),
            self.path == getattr(zipf, 'path', None),
        ])

    def __getitem__(self, addr):
        '''
        Return an address' body from the Zipfile using dict syntax.
        '''

        if addr in self:
            return self.read(addr)
        else:
            raise tools.errs.addr_not_exists(self.path, addr)

    def __hash__(self):
        '''
        Return the Zipfile's unique hash code.
        '''

        return hash('Zipfile:' + self.path)

    def __iter__(self):
        '''
        Yield each address in the Zipfile.
        '''

        with self.open('r') as zobj:
            yield from zobj.namelist()

    def __len__(self):
        '''
        Return the number of addresses in the Zipfile.
        '''

        with self.open('r') as zobj:
            return len(zobj.namelist())

    def __repr__(self):
        '''
        Return the Zipfile as a code-representative string.
        '''

        return f'Zipfile({self.path!r})'

    def create(self, addr, body):
        '''
        Create a new address in the Zipfile.
        '''

        if addr in self:
            raise tools.errs.addr_exists(self.path, addr)

        with self.open('a') as zobj:
            body = body.strip() + '\n'
            zobj.writestr(addr, body.encode('utf-8'))

    @contextlib.contextmanager
    def open(self, mode):
        '''
        Return a context manager for an open Zipfile object.
        '''

        try:
            zobj = zipfile.ZipFile(self.path, mode,
                compression   = self.__class__.compression,
                compresslevel = self.__class__.compresslevel,
            )
            yield zobj
        finally:
            zobj.close()

    def read(self, addr):
        '''
        Return the body of an address in the Zipfile.
        '''

        with self.open('r') as zobj:
            with zobj.open(addr, 'r') as fobj:
                return fobj.read().decode('utf-8')

    def read_dict(self):
        '''
        Return the entire Zipfile as an address-to-body dict.
        '''

        with self.open('r') as zobj:
            zdict = {}
            for addr in zobj.namelist():
                with zobj.open(addr, 'r') as fobj:
                    zdict[addr] = fobj.read().decode('utf-8')
            return zdict

    def update(self, addr, body):
        '''
        Overwrite an existing address in the Zipfile.
        '''

        if addr not in self:
            raise tools.errs.addr_not_exists(self.path, addr)

        zdict = self.read_dict()
        zdict[addr] = body

        with self.open('w') as zobj:
            for addr, body in zdict.items():
                body = body.strip() + '\n'
                zobj.writestr(addr, body.encode('utf-8'))
