import getopt
import sys

import c3srtconv


def usage():
    print('c3srtconv --offset=? --start=? --end=?\nall values in milliseconds.')


try:
    opts, args = getopt.getopt(sys.argv[1:], 'o:s:e:', ['offset=', 'start=', 'end='])
except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)

offset = None
start = None
end = None

for o, a in opts:
    if o in ('-o', '--offset'):
        offset = int(a)
    elif o in ('-s', '--start'):
        start = int(a)
    elif o in ('-e', '--end'):
        end = int(a)
    else:
        assert False, 'unhandled option ' + o

lines = c3srtconv.reader.read_multiple(sys.stdin)

if start is not None or end is not None:
    lines = c3srtconv.slice(lines, start, end)

lines = list(lines)

if len(lines) > 0:
    lines = c3srtconv.move_all(lines, lines[0].start_time * -1)

    if offset is not None:
        lines = c3srtconv.move_all(lines, offset)

srt = c3srtconv.writer.write_multiple(lines)

print(srt)
