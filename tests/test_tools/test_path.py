'''
Tests for 'soane.tools.path'.
'''

import os

from soane.tools import path

p = os.path.normpath

def test_base():
    # success
    assert path.base('/dire/file.ext') == 'file.ext'

def test_clean():
    # success
    assert path.clean('/dire/file.ext') == p('/dire/file.ext')

def test_dire():
    # success
    assert path.dire('/dire/file.ext') == '/dire'

def test_exists():
    # success
    assert path.exists(__file__)
    assert not path.exists('/nope.txt')

def test_expand():
    # setup
    os.environ['HOME'] = '/dire'
    os.environ['FILE'] = 'file.ext'
    os.environ['USERPROFILE'] = '/dire'

    # success
    assert path.expand('~/$FILE') == p('/dire/file.ext')

def test_ext():
    # success
    assert path.ext('/dire/file.ext') == 'ext'

def test_join():
    # success
    assert path.join('/dire', 'file.ext') == p('/dire/file.ext')

def test_name():
    # success
    assert path.name('/dire/file.ext') == 'file'
