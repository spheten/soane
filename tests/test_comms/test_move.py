'''
Tests for 'soane.comms.move'.
'''

from soane.comms.move import move

def test_move(cli):
    # success
    book, outs = cli(move, 'alpha', 'delta')
    assert outs == []
    assert 'alpha' not in book
    assert 'delta' in book

    # failure - nonexistent note
    book, outs = cli(move, 'nope', 'nope')
    assert outs == [
        "Error: the note 'nope' does not exist.\n",
    ]

    # failure - existing destination
    book, outs = cli(move, 'bravo', 'charlie')
    assert outs == [
        "Error: the note 'charlie' already exists.\n",
    ]
