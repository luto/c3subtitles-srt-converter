import c3srtconv


def test_write_single():
    str = c3srtconv.writer.write_single(c3srtconv.Line(5, 'A'))
    assert str == '00:00:00,005 --> 00:00:03,505\n' \
                  'A'

def test_write_multiple():
    str = c3srtconv.writer.write_multiple([
        c3srtconv.Line(1, 'A'),
        c3srtconv.Line(5, 'B')
    ])

    assert str == '1\n' \
                  '00:00:00,001 --> 00:00:03,501\n' \
                  'A\n' \
                  '\n' \
                  '2\n' \
                  '00:00:00,005 --> 00:00:03,505\n' \
                  'B\n\n'