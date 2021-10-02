'''
Tests for 'soane.tools.path'.
'''

import os

from soane.tools import path

PATH  = '/dire/file.ext'
CLEAN = PATH.replace('/', os.sep)

def test_base():
    # success
    assert path.base(PATH) == 'file.ext'

def test_clean():
    # success
    assert path.clean(PATH) == CLEAN

def test_dire():
    # success
    assert path.dire(PATH) == '/dire'

def test_expand():
    # setup
    os.environ['HOME'] = '/dire'
    os.environ['FILE'] = 'file.ext'
    os.environ['USERPROFILE'] = '/dire'

    # success
    assert path.expand('~/$FILE') == CLEAN

def test_ext():
    # success
    assert path.ext(PATH) == 'ext'

def test_join():
    # success
    assert path.join('/dire', 'file.ext') == CLEAN

def test_slug():
    # success
    assert path.slug('FILE-123!@#$') == 'file-123'

def test_stem():
    # success
    assert path.stem(PATH) == 'file'
