import c3srtconv


def test_read_single_line():
    line = c3srtconv.reader.read_single('1416437361274\tich bin ein live subs')

    assert line.start_time == 1416437361274
    assert line.text == 'ich bin ein live subs'


def test_read_multiple_lines():
    lines = c3srtconv.reader.read_multiple([
        '1416437361274\tich bin ein live subs',
        '1416437362798\tnice'
    ])

    assert len(lines) == 2

    assert lines[0].start_time == 1416437361274
    assert lines[0].text == 'ich bin ein live subs'

    assert lines[1].start_time == 1416437362798
    assert lines[1].text == 'nice'


def test_end_time():
    line = c3srtconv.Line(5, 'a bccc d')
    assert line.end_time == 11.5


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