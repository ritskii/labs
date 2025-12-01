#Варіант 2
#• Клас Temperature із приватною змінною _celsius.
#• Реалізуйте гетер і сетер, які конвертують температуру між °C та °F.

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9


t = Temperature(25)
print(t.fahrenheit)
t.fahrenheit = 212
print(t.celsius)
