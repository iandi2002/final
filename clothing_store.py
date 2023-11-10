# clothing_store.py
from observer import Observable, Observer

# Класс контекста, который будет использовать стратегию
class ClothingStore(Observable):
    def __init__(self, clothing_strategy):
        super().__init__()
        self.clothing_strategy = clothing_strategy

    def set_clothing_strategy(self, clothing_strategy):
        self.clothing_strategy = clothing_strategy

    def get_clothing_list(self):
        clothing_list = self.clothing_strategy.get_clothing_list()
        self.notify_observers("Catalog has been updated.")
        return clothing_list
