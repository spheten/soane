'''
Exception generation functions.
'''

def addr_exists(path, addr):
    '''
    Return an Exception for an existing zipfile address.
    '''

    return FileExistsError(
        f'address {addr!r} already exists in zipfile {path!r}',
    )

def addr_not_exists(path, addr):
    '''
    Return an Exception for a nonexistent zipfile address.
    '''

    return FileNotFoundError(
        f'address {addr!r} does not exist in zipfile {path!r}',
    )
