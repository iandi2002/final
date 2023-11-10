# discount_decorator.py
from decorator import ClothingDecorator

# Декоратор для добавления динамической скидки к ценам одежды
class DiscountDecorator(ClothingDecorator):
    def __init__(self, strategy, discounts):
        self.strategy = strategy
        self.discounts = discounts

    def get_clothing_list(self):
        clothing_list = self.strategy.get_clothing_list()
        discounted_clothing_list = [
            (item, self._apply_discount(item, price), price) for item, price in clothing_list
        ]
        return discounted_clothing_list

    def _apply_discount(self, item, price):
        item_discount = self.discounts.get(item, 0)
        discounted_price = price * (1 - item_discount / 100)
        return round(discounted_price, 2)
