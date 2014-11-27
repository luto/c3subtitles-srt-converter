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
