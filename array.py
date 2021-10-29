

class Array:
    def __init__(self, capacity, fill_value=None):
        self._items = list()
        for i in range(capacity):
            self._items.append(fill_value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, new_item):
        self._items[index] = new_item