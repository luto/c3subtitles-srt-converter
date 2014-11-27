import fileinput

import c3srtconv

lines = c3srtconv.reader.read_multiple(fileinput.input())
srt = c3srtconv.writer.write_multiple(lines)

print(srt)
