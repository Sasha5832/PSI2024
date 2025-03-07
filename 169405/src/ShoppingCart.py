class ShoppingCart:
    def __init__(self, items):
       if not isinstance(items, list):
           raise TypeError

       for elem in items:
           if not isinstance(elem, str):
               raise ValueError

       self.items = items.copy()

    def __str__(self):
        return f"Shopping card: {self.items}."

    def add_item(self, value):
        if not isinstance(value, str):
            raise ValueError
        self.items.append(value)

    def remove_intem(self, index):
        if not isinstance(index, int):
            raise TypeError

        if 0> index or index >= len(self.items):
            raise IndexError

        self.items.remove(self.items[index])


if __name__ == "__main__":
    s1 = ShoppingCart([])
    print(s1)
    s1.add_item("Apple")
    s1.add_item("Milk")
    print(s1)
    s1.remove_intem(0)
    print(s1)
