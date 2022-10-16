from flask_seeder import generator


sequence = generator.Sequence


class ListSequence(sequence):

    def __init__(self, data=[]):
        super().__init__(start=0, end=len(data))
        self.data = data

    def generate(self):
        value = self._next
        self._next += 1

        return self.data[value]
