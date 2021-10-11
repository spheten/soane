'''
Tests for 'soane.comms.rename'.
'''

from soane.comms.rename import rename

def test_rename(cli):
    # success
    book, outs = cli(rename, 'alpha', 'delta')
    assert outs == []
    assert 'alpha' not in book
    assert 'delta' in book

    # failure - nonexistent note
    book, outs = cli(rename, 'nope', 'nope')
    assert outs == [
        "Error: the note 'nope' does not exist.\n",
    ]

    # failure - existing destination
    book, outs = cli(rename, 'bravo', 'charlie')
    assert outs == [
        "Error: the note 'charlie' already exists.\n",
    ]
