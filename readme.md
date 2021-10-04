Soane
=====

[![](https://img.shields.io/github/last-commit/spheten/soane)][co]
[![](https://img.shields.io/pypi/pyversions/soane)][pp]
[![](https://img.shields.io/pypi/v/soane)][pp]
[![](https://img.shields.io/pypi/l/soane)][li]
[![](https://img.shields.io/github/issues-raw/spheten/soane)][is]

**Soane** (*Stephen's Old-Ass Note Engine*) is a command-line note manager, written and developed by Stephen Malone.

It's a deliberately crude system: the database is a single zip archive, the notes are all plaintext files and the commands are all braindead obvious. No magic, no sugar, no configuration, no nonsense.

If you just want to slap some CRUD on your notes and not bother with all that GUI nonsense, then Soane is for you. It's note-taking software for people who hate note-taking software.

- See [changes.md][ch] for development changes.
- See [license.md][li] for licensing information.

Installation
------------

Soane is available on [PyPi][pp]. To install, just run:

```text
$ pip install soane
```

or manually download the [latest release][la].

Setup
-----

**TODO:** Describe zipfile concepts and setup process.

Usage
-----

Soane supports command abbreviation, so you only need to type enough to disambiguate. For example, typing `soane r foo` will automatically translate to `soane read foo`.

### list GLOB

Print the names of all notes, or notes matching `GLOB` (default `*`).

```text
$ soane list
emily
lorelai
luke
rory
sookie

$ soane list l*
lorelai
luke
```

### read NAME

Print the contents of a note, if it exists.

```text
$ soane read lorelai
"I don't like Mondays, but unfortunately they come around eventually."
- Lorelai Gilmore
```

Contributions
-------------

If you experience a bug or have a feature suggestion, please submit it to the [issue tracker][is]. Thank you!

[ch]: https://github.com/spheten/soane/blob/master/changes.md
[co]: https://github.com/spheten/soane/commits/master
[is]: https://github.com/spheten/soane/issues
[la]: https://github.com/spheten/soane/releases/latest
[li]: https://github.com/spheten/soane/blob/master/license.md
[pp]: https://pypi.org/project/soane/
