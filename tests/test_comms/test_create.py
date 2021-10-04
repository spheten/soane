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
    assert "The note 'alpha' already exists." in outs[-1]
