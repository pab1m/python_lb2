from Stack import Stack


def sort_stack(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j].__len__() >= data[j + 1].__len__():
                data[j], data[j + 1] = data[j + 1], data[j]


def main():
    stacks = []
    n_stacks = int(input("Введіть кількість стеків: "))
    print()
    for i in range(n_stacks):
        stack = Stack()
        n = int(input(f"Введіть розмірність стеку {i + 1}: "))

        for j in range(n):
            element = int(input(f"Введіть {j + 1} елемент стеку: "))
            stack.append(element)
        print()

        print(f"Стек {i + 1}: {stack.items} \nКількість елементів = {stack.size()}")

        max_element = stack.max_element()
        stack.delete_el(max_element)

        min_element = stack.min_element()
        stack.delete_el(min_element)

        print(f"Видалені мінімальний та максимальний елементи із стеку {i + 1}: {[min_element, max_element]}")

        stacks.append(stack)
        print()

    new_stack = [stack.items for stack in stacks]

    print(f"Невідсортований масив: {new_stack}")
    sort_stack(new_stack)
    print(f"Відсортований масив: {new_stack}")


if __name__ == "__main__":
    main()
