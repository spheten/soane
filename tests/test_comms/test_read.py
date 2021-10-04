'''
Tests for 'soane.comms.read'.
'''

from soane.comms.read import read

def test_read(cli):
    # success
    assert cli(read, 'alpha') == [
        'Alpha note.\n',
    ]
