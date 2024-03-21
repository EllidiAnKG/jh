from abc import ABC, abstractmethod

class Inventory(ABC):
    def __init__(self):
        self.items = [] 

    def __len__(self):
        return len(self.items)

    def contains(self, item):
        return item in self.items  

    def add(self, item):
        self.items.append(item)  

    @abstractmethod
    def give_item(self, item):
        pass

class MyInventory(Inventory):
    def __init__(self):
        super().__init__()
        self.weapon = ["Меч", "Топор", "Лук"]
        self.armor = ["Шлем", "Нагрудник", "Ботинки"]
        self.potion = ["Зелье Регенерации", "Зелье Маны", "Зелье Выносливости"]
        self.materials = ["желеный Слиток", "Кожа", "Магическая эссенция"]

    def give_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return f"Предмет {item} получен из инвентаря."
        return f"Предмет {item} отсутствует в инвентаре."

my_inventory = MyInventory()


print("Оружие:")
print(", ".join(my_inventory.weapon))

print("Броня:")
print(", ".join(my_inventory.armor))

print("Зелья:")
print(", ".join(my_inventory.potion))

print("Материалы:")
print(", ".join(my_inventory.materials))
