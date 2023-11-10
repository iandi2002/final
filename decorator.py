# decorator.py

from abc import ABC, abstractmethod

# Определяем интерфейс декоратора
class ClothingDecorator(ABC):
    @abstractmethod
    def get_clothing_list(self):
        pass
