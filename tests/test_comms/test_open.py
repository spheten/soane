'''
Tests for 'soane.comms.open'.
'''

import click

from soane.comms.open import open_

def test_open_(cli, monkeypatch):
    # setup
    opens = []
    func  = lambda path: opens.append(path)
    monkeypatch.setattr(click, 'launch', func)

    # success
    book, outs = cli(open_, 'alpha')
    assert opens == [book['alpha'].path]

    # failure - nonexistent note
    book, outs = cli(open_, 'nope')
    assert outs == [
        "Error: the note 'nope' does not exist.\n",
    ]
