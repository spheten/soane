'''
Tests for 'soane.comms._base'.
'''

from soane.comms import _base

def test_soane(cli):
    # success
    assert cli(_base.soane, 'read', 'alpha') == [
        'Alpha note.\n', '\n',
    ]
