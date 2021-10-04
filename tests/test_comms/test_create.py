'''
Tests for 'soane.comms.create'.
'''

from soane.comms.create import create

def test_read(cli):
    # success
    book, outs = cli(create, 'delta')
    assert book['delta'].exists()
    assert outs == []

    # failure - existing note
    book, outs = cli(create, 'alpha')
    assert outs == [
        "Error: The note 'alpha' already exists.\n",
    ]
