import c3srtconv


def write_single(line):
    start_time = c3srtconv.time_to_srt_str(line.start_time)
    end_time = c3srtconv.time_to_srt_str(line.end_time)
    return "{} --> {}\n{}".format(start_time, end_time, line.text)


def write_multiple(lines):
    srt = ''
    num = 0

    for line in lines:
        num += 1
        srt += str(num) + '\n' + write_single(line) + '\n\n'

    return srt