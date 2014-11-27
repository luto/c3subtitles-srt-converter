# c3subtitles-srt-converter

## Development

### Setup

use py3.

```
$ virtualenv venv
$ pip install -r requirements.txt
$ test.py   # run unittests
```

## Usage
```
$ python -m c3srtconv --start=100 --end=500 --offset=50 < some_dump_file.txt
```

Print the dump contained in `some_dump_file.txt` as SRT to standard output. Take only lines between time `100` and
`500` in milliseconds. If no offset is given `100` will be the new temporary zero. If one is given, as in the this
case the offset (`50`) will be added to all lines. So the first lines is `00:00:00,050`.

### input format

Lines of `millisecond, tab, text`, for example:

```
1417087782881	Foo
1417087784728	Bar
1417087786618	Moo
1417087790883	Test 2 3 4 
```
