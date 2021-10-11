'''
Tests for 'soane.comms.create'.
'''

import click

from soane.comms.create import create

def test_read(cli, monkeypatch):
    # setup
    opens = []
    func  = lambda path: opens.append(path)
    monkeypatch.setattr(click, 'launch', func)

    # success
    book, outs = cli(create, 'delta')
    assert book['delta'].exists()
    assert outs == []

    # success - with --open
    book, outs = cli(create, 'echo', '--open-after')
    assert book['echo'].exists()
    assert outs == []
    assert opens == [book['echo'].path]

    # failure - existing note
    book, outs = cli(create, 'alpha')
    assert outs == [
        "Error: the note 'alpha' already exists.\n",
    ]
