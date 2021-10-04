'''
Tests for 'soane.comms._base'.
'''

from soane.comms import _base

def test_group(cli):
    # success
    assert cli(_base.group, 'read', 'alpha') == [
        'Alpha note.\n',
    ]
