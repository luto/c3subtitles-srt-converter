import c3srtconv


def test_fix_offset():
    lines = [
        c3srtconv.Line(200, 'A'),
        c3srtconv.Line(250, 'B'),
    ]

    new_lines = c3srtconv.fix_offset(lines, 100)

    assert len(lines) == 2
    assert lines[0].start_time == 200
    assert lines[0].text == 'A'
    assert lines[1].start_time == 250
    assert lines[1].text == 'B'

    assert len(new_lines) == 2
    assert new_lines[0].start_time == 100
    assert new_lines[0].text == 'A'
    assert new_lines[1].start_time == 150
    assert new_lines[1].text == 'B'


def test_time_to_srt_str():
    str = c3srtconv.time_to_srt_str(7105021)
    assert str == '01:58:25,021'


def test_slice_start_end():
    lines = c3srtconv.slice([
        c3srtconv.Line(0, 'A'),
        c3srtconv.Line(1, 'B'),
        c3srtconv.Line(2, 'C'),
        c3srtconv.Line(3, 'D'),
        c3srtconv.Line(4, 'E'),
        c3srtconv.Line(5, 'F'),
    ], 2, 4)

    lines = list(lines)

    assert len(lines) == 3
    assert lines[0].text == 'C'
    assert lines[1].text == 'D'
    assert lines[2].text == 'E'


def test_slice_start():
    lines = c3srtconv.slice([
        c3srtconv.Line(0, 'A'),
        c3srtconv.Line(1, 'B'),
        c3srtconv.Line(2, 'C'),
        c3srtconv.Line(3, 'D'),
        c3srtconv.Line(4, 'E'),
        c3srtconv.Line(5, 'F'),
    ], 2)

    lines = list(lines)

    assert len(lines) == 4
    assert lines[0].text == 'C'
    assert lines[1].text == 'D'
    assert lines[2].text == 'E'
    assert lines[3].text == 'F'


def test_slice_end():
    lines = c3srtconv.slice([
        c3srtconv.Line(0, 'A'),
        c3srtconv.Line(1, 'B'),
        c3srtconv.Line(2, 'C'),
        c3srtconv.Line(3, 'D'),
        c3srtconv.Line(4, 'E'),
        c3srtconv.Line(5, 'F'),
    ], end=2)

    lines = list(lines)

    assert len(lines) == 3
    assert lines[0].text == 'A'
    assert lines[1].text == 'B'
    assert lines[2].text == 'C'
