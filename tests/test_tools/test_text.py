'''
Tests for 'soane.tools.text'.
'''

from soane.tools import text

def test_disambiguate():
    # setup
    names = ['test-one', 'test-two']

    # success
    assert text.disambiguate('test-one', names) == ['test-one']
    assert text.disambiguate('test-o',   names) == ['test-one']
    assert text.disambiguate('test',     names) == ['test-one', 'test-two']
    assert text.disambiguate('nope',     names) == []

def test_glob():
    # success
    assert text.glob('alpha', 'alpha')
    assert text.glob('alpha', 'alp??')
    assert not text.glob('alpha', 'nope')
