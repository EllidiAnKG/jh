from abc import ABC, abstractmethod
class Inventory(ABC):
    def __init__(self):
        self.items = []  # Инициализация списка предметов

    def __len__(self):
        return len(self.items)  # Длина инвентаря

    def __contains__(self, item):
        return item in self.items  # Проверка наличия предмета в инвентаре

    def add(self, item):
        self.items.append(item)  # Добавление предмета в инвентарь

    @abstractmethod
    def give_item(self, item):
        pass


class MyInventory(Inventory):
    def __init__(self):
        super().__init__()


    def give_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return f"Предмет {item} получен из инвентаря."
        return f"Предмет {item} отсутствует в инвентаре."

my_inventory =  MyInventory()


my_inventory.add("Меч")
my_inventory.add("Магический посох")


print("Длина инвентаря:", len(my_inventory))


print("Наличие Меча в инвентаре:", my_inventory.__contains__("Меч"))


print(my_inventory.give_item("Меч"))
print(my_inventory.give_item("Книга заклинаний"))