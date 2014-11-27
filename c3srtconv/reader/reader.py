from c3srtconv import Line

class ParseException(Exception):
    def __init__(self, msg):
        super(ParseException, self).__init__(msg)


def read_single(line):
    parts = line.split('\t', 2)

    if len(parts) == 0:
        raise ParseException('line does not contain a tab')

    try:
        start_time = int(parts[0])
    except ValueError:
        raise ParseException('lines has an non-numeric timestamp')

    text = parts[1]

    return Line(start_time, text)


def read_multiple(lines):
    return [read_single(line) for line in lines]
