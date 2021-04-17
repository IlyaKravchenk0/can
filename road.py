class Road:
    'Родительский класс'
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    "Дочерний класс"
    def init(self, _length, _width):
        super().__init__(_length, _width)



r = MassCount(25, 10000)
print(r.mass())