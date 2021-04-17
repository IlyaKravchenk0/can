class Stationery:
    "Родительский класс"
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Отрисовка')


class Pen(Stationery):
    "Дочерний класс"
    def draw(self):
        print(f'Отрисовка тонкой линии с помощью {self.title}')

class Pancil(Stationery):
    "Дочерний класс"
    def draw(self):
        print(f'Чертим обьекты с помошью {self.title}')

class Handle(Stationery):
    "Дочерний класс"
    def draw(self):
        print(f'Замазываем не нужные слова с помощью {self.title}')

pen = Pen('ручки')
pancil = Pancil('карандаша')
handler = Handle('маркера')

pen.draw()
pancil.draw()
handler.draw()