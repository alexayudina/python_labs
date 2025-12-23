from typing import Optional, Any


class Node:
    """
    Класс Node представляет узел односвязного списка.
    Каждый узел хранит значение и ссылку на следующий узел.
    """
    
    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        # Значение, которое хранит узел (любого типа)
        self.value = value
        
        # Ссылка на следующий узел в списке
        # None означает, что это последний узел
        self.next = next_node  # Здесь сохраняем как self.next


class SinglyLinkedList:
    """
    Класс SinglyLinkedList реализует односвязный список.
    Состоит из узлов Node, связанных друг с другом через ссылки next.
    """
    
    def __init__(self, items: Optional[list] = None):
        # Голова списка - первый узел или None если список пуст
        self.head = None
        
        # Количество элементов в списке (для быстрого получения длины)
        self._size = 0
        
        # Опционально: инициализация списка начальными значениями
        if items:
            for item in items:
                self.append(item)

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка."""
        new_node = Node(value)  # Создаем новый узел

        # Если список пуст, новый узел становится головой
        if self.head is None:
            self.head = new_node
            self._size += 1
            return

        # Иначе проходим до последнего узла
        current = self.head
        while current.next is not None:  # Ищем узел, у которого next = None
            current = current.next

        # Добавляем новый узел после последнего
        current.next = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка."""
        # Создаем новый узел, который ссылается на текущую голову
        new_node = Node(value, next_node=self.head)  # Используем next_node
        
        # Новый узел становится новой головой
        self.head = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """
        Вставить элемент по указанному индексу.
        
        Args:
            idx: Индекс для вставки (от 0 до размера списка)
            value: Значение для вставки
            
        Raises:
            IndexError: Если индекс вне допустимого диапазона
        """
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        # Вставка в начало - используем prepend
        if idx == 0:
            self.prepend(value)
            return

        # Создаем новый узел
        new_node = Node(value)

        # Находим узел, который будет предшествовать новому
        current = self.head
        for _ in range(idx - 1):
            current = current.next  # Безопасно, так как idx <= _size

        # Вставляем новый узел между current и current.next
        new_node.next = current.next  # Новый узел ссылается на следующий
        current.next = new_node       # Текущий узел ссылается на новый
        self._size += 1

    def remove_at(self, idx: int) -> None:
        """
        Удалить элемент по указанному индексу.
        
        Args:
            idx: Индекс элемента для удаления
            
        Raises:
            IndexError: Если индекс вне допустимого диапазона
        """
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        # Удаление первого элемента (особый случай)
        if idx == 0:
            self.head = self.head.next  # Просто пропускаем первый узел
            self._size -= 1
            return

        # Находим узел, предшествующий удаляемому
        current = self.head
        for _ in range(idx - 1):
            current = current.next

        # Пропускаем удаляемый узел
        # current.next - это удаляемый узел
        # current.next.next - это узел после удаляемого
        current.next = current.next.next
        self._size -= 1

    def remove(self, value: Any) -> bool:
        """
        Удалить первое вхождение указанного значения.
        
        Returns:
            True если элемент был найден и удален, иначе False
        """
        if self.head is None:  # Список пуст
            return False
            
        # Если удаляемый элемент - голова списка
        if self.head.value == value:
            self.head = self.head.next  # Пропускаем голову
            self._size -= 1
            return True

        # Ищем узел с нужным значением
        current = self.head
        while current.next is not None:  # Проверяем следующий узел
            if current.next.value == value:
                # Нашли - пропускаем этот узел
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next  # Переходим к следующему узлу
            
        return False  # Элемент не найден

    def __iter__(self):
        """
        Итератор для обхода значений списка.
        
        Yields:
            Значения узлов от головы к хвосту
        """
        current = self.head
        while current is not None:
            yield current.value  # Возвращаем значение текущего узла
            current = current.next  # Переходим к следующему узлу

    def __len__(self) -> int:
        """Вернуть количество элементов в списке."""
        return self._size

    def __repr__(self) -> str:
        """Формальное строковое представление списка."""
        values = list(self)  # Преобразуем итератор в список
        return f"SinglyLinkedList({values})"

    def plotter(self) -> str:
        """
        Визуальное представление списка в виде цепочки узлов.
        
        Returns:
            Строка вида: [A] -> [B] -> [C] -> None
        """
        parts = []
        current = self.head
        
        # Собираем значения всех узлов
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
            
        # Добавляем None в конце для наглядности
        parts.append("None")
        
        # Соединяем стрелками
        return " -> ".join(parts)


ll = SinglyLinkedList()
ll.append(10)
ll.prepend(5)
ll.insert(1, 7)
print(ll.plotter())  # [5] -> [7] -> [10] -> None
ll.remove_at(1)
print(ll.plotter())  # [5] -> [10] -> None