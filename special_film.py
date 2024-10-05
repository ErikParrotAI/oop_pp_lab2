from film import Film
from category import Category

class SpecialFilm(Film, Category):
    def __init__(self, title, director, duration, num_actors, category_name):
        # Викликаємо конструктори обох батьківських класів
        Film.__init__(self, title, director, duration, num_actors)
        Category.__init__(self, category_name)

    # Перевизначаємо метод __str__, щоб включити інформацію про категорію
    def __str__(self):
        return f"{super().__str__()}, {self.describe()}"
