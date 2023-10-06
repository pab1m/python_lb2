class Stack:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def pop(self):
        if self.size() != 0:
            self.items.pop()
        else:
            return print("Стек порожній")

    def delete_el(self, el):
        if self.size() != 0:
            self.items.remove(el)
        else:
            return print("Стек порожній")

    def min_element(self):
        if self.size() != 0:
            return min(self.items)
        else:
            return print("Стек порожній")

    def max_element(self):
        if self.size() != 0:
            return max(self.items)
        else:
            return print("Стек порожній")
