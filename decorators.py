# Декоратор для методів
def show_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається метод: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Метод {func.__name__} завершився")
        return result
    return wrapper
