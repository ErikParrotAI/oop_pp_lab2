from decorators import show_decorator

class Film:
    # Атрибут класу (наприклад, курс долара)
    exchange_rate = 1.0  # Статичний атрибут класу

    # Конструктор з параметрами
    def __init__(self, title="Невідомий фільм", director="Невідомий режисер", duration=0, num_actors=0):
        self._title = title  # Приватний атрибут
        self._director = director
        self.duration = duration
        self.num_actors = num_actors

    # Властивість для назви фільму
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) > 0:
            self._title = value

    # Метод для розрахунку вартості з декоратором
    @show_decorator
    def cost(self):
        cost = self.duration * 20 + self.num_actors * 30
        if self._director in ["Стівен Спілберг", "Джеймс Кемерон"]:
            cost *= 2
        return cost * Film.exchange_rate  # Використовуємо статичний атрибут

    # Метод __str__ для строкового подання
    def __str__(self):
        return f"Фільм: {self.title}, Режисер: {self._director}, Тривалість: {self.duration} хв., Акторів: {self.num_actors}"

    # Статичний метод для зміни курсу
    @staticmethod
    def set_exchange_rate(rate):
        Film.exchange_rate = rate
