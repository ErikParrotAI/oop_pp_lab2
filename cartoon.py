from film import Film
from decorators import show_decorator

class Cartoon(Film):
    # Перевизначаємо метод cost для мультфільму з декоратором
    @show_decorator
    def cost(self):
        return self.duration * 25 + self.num_actors * 10
