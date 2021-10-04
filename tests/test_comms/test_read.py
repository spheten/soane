'''
Tests for 'soane.comms.read'.
'''

from soane.comms.read import read

def test_read(cli):
    # success
    book, outs = cli(read, 'alpha')
    assert outs == ['Alpha note.\n']
