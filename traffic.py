
# Импортируем библеотеку для работы со временем
from time import sleep

# Создаем класс
class TrafficLight:
    # Атрибуты класса
    __color = 'red'
    #Конструкцию класса
    def __init__(self):
        self.__color = TrafficLight.__color # ЭКземпляр класса
        print('Внимание, светофор!')

    # Метод класса
    def running(self):
        print('Красный!')
        sleep(7)
        print('Желтый!')
        sleep(2)
        print('Зеленый!')
        print('Поехали!!!')


light = TrafficLight()
light.running()