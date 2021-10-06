'''
Tests for 'soane.comms.delete'.
'''

from soane.comms.delete import delete

def test_delete(cli):
    # success
    book, outs = cli(delete, 'alpha')
    assert outs == []
    assert 'alpha' not in book

    # failure - nonexistent note
    book, outs = cli(delete, 'nope')
    assert outs == [
        "Error: the note 'nope' does not exist.\n",
    ]
