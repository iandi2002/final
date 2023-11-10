# factory.py

from abc import ABC, abstractmethod
from main import WomenClothing, MenClothing, KidsClothing, SportClothing
from discount_decorator import DiscountDecorator
from main import ClothingStrategy, PriceAdapter

# Фабрика для создания стратегий одежды
class ClothingStrategyFactory:
    @staticmethod
    def create_strategy(choice ):
        if choice  == "1":
            return WomenClothing()
        elif choice  == "2":
            return MenClothing()
        elif choice  == "3":
            return KidsClothing()
        elif choice  == "4":
            return SportClothing()
        else:
            raise ValueError("Invalid strategy type")

