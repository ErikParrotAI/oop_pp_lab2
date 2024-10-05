class Category:
    def __init__(self, category_name="Uncategorized"):
        self.category_name = category_name

    def describe(self):
        return f"Категорія: {self.category_name}"
