import datetime


class Line:
    def __init__(self, start_time, text):
        self._start_time = start_time
        self._text = text
        self._end_time = self._calculate_end_time()

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def text(self):
        return self._text

    def count_words(self):
        return self._text.count(' ') + 1

    def _calculate_end_time(self):
        duration = 2 + self.count_words() * 1.5
        return self.start_time + duration

    def fix_offset(self, offset):
        return Line(self._start_time - offset, self._text)
