from datetime import datetime


def fix_offset(lines, offset):
    return [line.fix_offset(offset) for line in lines]


def time_to_srt_str(time):
    ms = int(time % 1000)
    time //= 1000

    s = int(time % 60)
    time //= 60

    m = int(time % 60)
    time //= 60

    h = int(time % 60)

    return '{0:02d}:{1:02d}:{2:02d},{3:03d}'.format(h, m, s, ms)
