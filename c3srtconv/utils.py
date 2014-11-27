from datetime import datetime


def move_all(lines, offset):
    return [line.move(offset) for line in lines]


def slice(lines, start=None, end=None):
    for line in lines:
        if (start is None or line.start_time >= start) and \
           (end is None or line.start_time <= end):
            yield line
            continue


def time_to_srt_str(time):
    ms = int(time % 1000)
    time //= 1000

    s = int(time % 60)
    time //= 60

    m = int(time % 60)
    time //= 60

    h = int(time % 60)

    return '{0:02d}:{1:02d}:{2:02d},{3:03d}'.format(h, m, s, ms)
