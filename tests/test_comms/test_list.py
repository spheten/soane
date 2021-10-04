'''
Tests for 'soane.comms.list'.
'''

from soane.comms.list import list_

def test_list_(cli):
    # success - default GLOB
    book, outs = cli(list_)
    assert outs == ['alpha\n', 'bravo\n', 'charlie\n']

    # success - custom GLOB
    book, outs = cli(list_, 'a*')
    assert outs == ['alpha\n']
