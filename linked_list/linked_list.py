class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0
        self._last_added_value = None

    def __getitem__(self, index):
        current = self.__head
        for _ in range(index):
            if current is None or current.has_next():
                raise IndexError
            current = current.get_next()
        return current.value

    def __len__(self):
        return self.__len

    # Add "__contains__" method
    def __contains__(self, value):
        current = self.__head
        for _ in range(self.__len):
            if value is current.value:
                return True
            else:
                current = current.get_next()
        return False

    # Modify "add" method:
    def add(self, value, index=None):
        self.__len += 1
        new_item = LinkedListItem(value)
        # if there is no index
        if index is None:
            if not self.__head:
                self.__head = new_item
            else:
                self.__tail.set_next(new_item)
            self.__tail = new_item
            self._last_added_value = self.__tail.value
        else:
            # if the linked list is empty
            if not self.__head:
                if index == 0:
                    self.__head = new_item
                    self.__tail = new_item
                    self._last_added_value = self.__tail.value
                    return
                elif index != 0:
                    raise IndexError(f"Invalid position ({index})")
            # if linked list is not empty
            # insert at the beginning of the list
            if index == 0:
                new_item.set_next(self.__head)
                self.__head = new_item
                self._last_added_value = self.__head.value
            # insert at a given position
            if index > 0:
                current = self.__head
                for _ in range(index - 1):
                    if current is None or current.has_next():
                        raise IndexError
                    current = current.get_next()
                if current:
                    new_item.set_next(current.get_next())
                    current.set_next(new_item)
                    self._last_added_value = current.get_next().value
                else:
                    raise IndexError

    # Add and modify "add_all" method:
    def add_all(self, list_of_el, position=None):
        if position is None:
            for el in list_of_el:
                self.add(el)
        else:
            pos = position
            for el in list_of_el:
                self.add(el, pos)
                pos += 1

    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value

    # Add "pop" method:
    def pop(self, index=None):
        # if there is no index
        # delete and return the last element
        if index is None:
            del_el = self.__tail.value
            current = self.__head
            for _ in range(self.__len - 2):
                if current is None or current.has_next():
                    raise IndexError
                current = current.get_next()
            current.set_next(None)
            self.__tail = current.value
            self.__len -= 1
            return del_el
        else:
            # if the linked list is empty
            if self.__head is None:
                raise IndexError("Empty linked list")
            # if the linked list is not empty
            del_el = self.__getitem__(index)
            if index < 0:
                raise IndexError
            if index == 0:
                self.__head = self.__head.get_next()
                return del_el
            count = 0
            current = self.__head
            prev = self.__head
            temp = self.__head
            while current is not None:
                if count == index:
                    temp = current.get_next()
                    break
                prev = current
                current = current.get_next()
                count += 1
            prev.set_next(temp)
            self.__len -= 1
            return del_el

    # Add "remove_last_occurrence" method:
    def remove_last_occurrence(self, value):
        indexes = []
        current = self.__head
        for el in range(self.__len):
            if current.value == value:
                indexes.append(el)
            current = current.get_next()
        if len(indexes) == 0:
            raise IndexError("There is no such value in a list")
        else:
            self.pop(indexes[-1])

    # Add "print_list" method to check the values in a linked list:
    def print_list(self):
        current = self.__head
        while current:
            print(current.value, end=" ")
            current = current.get_next()


if __name__ == "__main__":
    items = LinkedList()
    items.add(1)
    items.add(2, 10)
    items.add(3)
    items.print_list()
    print("1 in a linked list: ", 1 in items)
    items.add(5, 0)
    items.add(6, 0)
    items.add(7, 2)
    items.print_list()
    print("10 in a linked list: ", 10 in items)
    items.add_all([100, 101], 2)
    items.print_list()
    print(items[1])
    print(items[2])
    print(items.first())
    print(items.last())
    print(len(items))
    print("Pop", items.pop())
    items.print_list()
    items.remove_last_occurrence(10)
    print()
    items.print_list()
    print(10 in items)
