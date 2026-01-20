class Stack:
    def __init__(self):
        """Инициализация пустого стека"""
        self._items = []  # защищенный атрибут

    def is_empty(self):
        """Проверка стека на пустоту. Возвращает True или False"""
        return len(self._items) == 0

    def push(self, item):
        """Добавляет новый элемент на вершину стека"""
        self._items.append(item)

    def pop(self):
        """Удаляет верхний элемент стека. Возвращает верхний элемент"""
        if not self.is_empty():
            return self._items.pop()
        raise IndexError("Попытка удалить элемент из пустого стека")

    def peek(self):
        """Возвращает верхний элемент стека, но не удаляет его"""
        if not self.is_empty():
            return self._items[-1]
        raise IndexError("Попытка посмотреть элемент в пустом стеке")

    def size(self):
        """Возвращает количество элементов в стеке"""
        return len(self._items)

    def __str__(self):
        """Строковое представление стека (для отладки)"""
        return str(self._items)


def is_balanced(brackets_string):
    """
    Проверяет сбалансированность скобок в строке
    Возвращает True если скобки сбалансированы, иначе False
    """
    stack = Stack()

    # Пары скобок
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in brackets_string:
        if char in '([{':  # открывающая скобка
            stack.push(char)
        elif char in ')]}':  # закрывающая скобка
            # Если стек пуст или последняя открывающая скобка не соответствует текущей закрывающей
            if stack.is_empty() or stack.peek() != pairs[char]:
                return False
            stack.pop()  # удаляем соответствующую открывающую скобку

    # В конце стек должен быть пуст
    return stack.is_empty()


def check_brackets(brackets_string):
    """
    Проверяет строку со скобками и возвращает понятное сообщение
    """
    if is_balanced(brackets_string):
        return "Сбалансированно"
    else:
        return "Несбалансированно"


def main():
    """Основная функция для демонстрации работы"""
    print("=" * 60)
    print("Демонстрация работы стека:")
    print("=" * 60)

    # Пример использования стека
    stack = Stack()

    print("1. Создаем стек и добавляем элементы:")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"   Стек после push(1), push(2), push(3): {stack}")
    print(f"   Размер стека: {stack.size()}")
    print(f"   Верхний элемент (peek): {stack.peek()}")
    print(f"   Стек пуст? {stack.is_empty()}")

    print("\n2. Удаляем элементы:")
    print(f"   pop(): {stack.pop()}")
    print(f"   Стек теперь: {stack}")
    print(f"   pop(): {stack.pop()}")
    print(f"   Стек теперь: {stack}")

    print("\n" + "=" * 60)
    print("Проверка сбалансированности скобок:")
    print("=" * 60)

    # Тестовые примеры из задания
    tests = [
        ("(((([{}]))))", True),
        ("[([])((([[[]]])))]{()}", True),
        ("{{[()]}}", True),
        ("}{}", False),
        ("{{[(])]}}", False),
        ("[[{())}]", False),
        ("", True),  # пустая строка считается сбалансированной
        ("()", True),
        ("([])", True),
        ("([)]", False)
    ]

    for test_str, expected in tests:
        result = is_balanced(test_str)
        status = "✓" if result == expected else "✗"
        print(
            f"{status} '{test_str:25}' -> {check_brackets(test_str):20} (ожидалось: {'Сбалансированно' if expected else 'Несбалансированно'})")

    print("\n" + "=" * 60)
    print("Интерактивная проверка:")
    print("=" * 60)

    # Интерактивный режим
    while True:
        user_input = input("\nВведите строку со скобками (или 'выход' для завершения): ")
        if user_input.lower() in ['выход', 'exit', 'quit']:
            break
        print(f"Результат: {check_brackets(user_input)}")


if __name__ == "__main__":
    main()