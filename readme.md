Soane
=====

[![](https://img.shields.io/github/last-commit/spheten/soane)][co]
[![](https://img.shields.io/pypi/pyversions/soane)][pp]
[![](https://img.shields.io/pypi/v/soane)][ch]
[![](https://img.shields.io/pypi/l/soane)][li]
[![](https://img.shields.io/github/issues-raw/spheten/soane)][is]

**Soane** (*Stephen's Old-Ass Note Engine*) is a command-line note manager, written and developed by Stephen Malone. Elevator pitch: it's a CLI made of CRUD for all your TXTs.

Here's how it works:

- **Your notes** are plaintext files kept in a single directory of your choosing.
- **The configuration** is two easy environment variables.
- **The commands** operate on those files in super handy ways.

Why do you need this? If you like text files but hate staring at the file manager, if you want to record information and actually find it later, if you have "summon terminal" bound to a keystroke, then Soane is for you.

Installation
------------

Soane is available on [PyPi][pp]. To install, just run:

```text
$ pip install soane
```

or manually download the [latest release][la].

Setup
-----

Soane only requires two environment variables for configuration:

```bash
# The path to your notes directory. Tildes and variables welcome.
SOANE_DIR = "~/path/to/notes"

# The file extension your notes use. No leading dot, please.
SOANE_EXT = "txt"
```

Set these variables and you're good to go. On Windows, go to System Properties or search for "environment variables" in Start; on Linux and Mac you'll need to edit a dotfile in your home directory.

Usage
-----

### Basic Advice

- Commands can be abbreviated, so `soane r foo` automatically expands to `soane read foo`.
- Notes are referenced by basename, so a file named `notes/foo.txt` is called `foo`.
- All commands have built-in help, so start with `soane --help` and look around!

### `create NAME [-o]`

Create a new empty note called `NAME`.

```bash
$ soane create dean
# Creates the empty file 'dean' in your notes directory.
```

To open the note immediately after creation, add `-o / --open-after`:

```bash
$ soane create jess -o
# Creates 'jess' and opens it in your default text editor.
```

### `delete NAME`

Delete the note called `NAME` by sending it to your operating system trash.

```bash
$ soane delete tristan
# Sends 'tristan' to your operating system trash.
```

### `list GLOB`

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

### `open NAME`

Open a note in your default text editor.

```bash
$ soane open emily
# Opens 'emily' in your default editor for SOANE_EXT.
```

### `read NAME`

Print the contents of a note, if it exists.

```text
$ soane read lorelai
“As long as everything is exactly the way I want it, I'm totally flexible.”
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
