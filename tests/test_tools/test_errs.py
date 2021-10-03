'''
Tests for 'soane.tools.errs'.
'''

from soane.tools import errs

def test_addr_exists():
    # success
    exc = errs.addr_exists('path', 'addr')
    assert str(exc) == "address 'addr' already exists in zipfile 'path'"

def test_addr_not_exists():
    # success
    exc = errs.addr_not_exists('path', 'addr')
    assert str(exc) == "address 'addr' does not exist in zipfile 'path'"
