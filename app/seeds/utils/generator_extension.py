from datetime import datetime, timedelta, timezone
from pathlib import Path
import random
from flask_seeder import generator


sequence = generator.Sequence


def read_resource(path):
    names = []
    with open(Path(path).absolute()) as source:
        names = source.read().splitlines()

    return names


class NameSequence(sequence):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._lines = None

    def generate(self):
        if self._lines is None:
            self._lines = read_resource("app/seeds/utils/names/names.txt")

        result = self.rnd.choice(self._lines)

        return result


class ListSequence(sequence):

    def __init__(self, data=[]):
        super().__init__(start=0, end=len(data))
        self.data = data

    def generate(self):
        value = self._next
        self._next += 1

        return self.data[value]


class DateSequence(sequence):

    def __init__(self, start_date: datetime, **kwargs):
        super().__init__(**kwargs)
        self.start_date = start_date

    def generate(self):
        days = timedelta(days=8)
        end_date = datetime.now(timezone.utc)
        random_date = self.start_date + \
            random.randrange((end_date - self.start_date) // days + 1) * days

        return random_date
