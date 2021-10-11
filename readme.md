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

- Commands can be abbreviated, so `soane l` automatically expands to `soane list`.
- Notes are referenced by base filename, so `notes/foo.txt` is called `foo`.
- All commands have built-in help, so start with `soane --help` and look around!

### `create NAME [-o]`

Create a new empty note file.

```bash
$ soane create bojack
# Creates the empty file 'bojack' in your notes directory.
```

To open the note immediately after creation, add `-o / --open-after`:

```bash
$ soane create bojack -o
# Creates 'bojack' and opens it in your default text editor.
```

### `delete NAME`

Delete a note by sending it to your operating system trash.

```bash
$ soane delete sarah
# Sends 'sarah' to your operating system trash.
```

### `list GLOB`

Print the names of all notes, or notes matching `GLOB` (default `*`).

```bash
$ soane list
bojack
carolyn
diane
peanutbutter
todd

$ soane list pea*
peanutbutter
```

### `move` NAME DEST`

move a note to a new name, if that name doesn't already exist.

```text
$ soane `move` carolyn princess-carolyn
```

### `open NAME`

Open a note in your default text editor.

```bash
$ soane open bojack
# Opens 'bojack' in your default editor for SOANE_EXT.
```

### `read NAME`

Print the contents of a note, if it exists.

```text
$ soane read bojack
“I’m responsible for my own happiness? I can’t even be responsible
for my own breakfast.”
- Bojack Horseman
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
