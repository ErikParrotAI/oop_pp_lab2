from film import Film
from cartoon import Cartoon
from special_film import SpecialFilm

# Демонстраційна програма
def demo():
    # Створюємо екземпляр класу Фільм
    film = Film("Jurassic Park", "Стівен Спілберг", 127, 15)
    print(film)
    print(f"Вартість фільму: {film.cost()} тис. доларів")

    # Створюємо екземпляр класу Мультфільм
    cartoon = Cartoon("Toy Story", "Джон Лассетер", 81, 8)
    print(cartoon)
    print(f"Вартість мультфільму: {cartoon.cost()} тис. доларів")

    # Створюємо екземпляр класу SpecialFilm (множинне наслідування)
    special_film = SpecialFilm("Avatar", "Джеймс Кемерон", 162, 30, "Наукова фантастика")
    print(special_film)
    print(f"Вартість спеціального фільму: {special_film.cost()} тис. доларів")


# Запуск демонстрації
if __name__ == "__main__":
    demo()
