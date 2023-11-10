# main.py
from abc import ABC, abstractmethod
from decorator import ClothingDecorator
from discount_decorator import DiscountDecorator
import locale
from observer import Observer
from observer import Observable
from clothing_store_observer import ClothingStoreObserver


# Определяем интерфейс стратегии
class ClothingStrategy(ABC):
    @abstractmethod
    def get_clothing_list(self):
        pass

# Конкретные стратегии
class WomenClothing(ClothingStrategy):
    def get_clothing_list(self):
        return [("Jeans", 50), ("Blouse", 30)]

class MenClothing(ClothingStrategy):
    def get_clothing_list(self):
        return [("Trousers", 70), ("Shirt", 40)]

class KidsClothing(ClothingStrategy):
    def get_clothing_list(self):
        return [("Boots", 60), ("Cap", 15)]

class SportClothing(ClothingStrategy):
    def get_clothing_list(self):
        return [("Running Shoes", 80), ("Sport T-shirt", 35)]


# Адаптер для отображения цен в тенге и долларах
class PriceAdapter:

    def __init__(self, strategy):
        self.strategy = strategy

    def get_clothing_list(self):
        clothing_list = self.strategy.get_clothing_list()

        clothing_list = [(item, self._convert_to_tenge(price))
                         for item, price in clothing_list]

        return clothing_list

    def _convert_to_tenge(self, price_usd):
        exchange_rate = 422.40

        price_tenge = round(price_usd * exchange_rate, 2)
        return price_tenge

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

# Singleton для аутентификации пользователя
class UserAuthenticationSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def authenticate_user(self, username, password):
        # Perform authentication logic here
        valid_users = {"password1": "password1", "2": "2"}  # Replace with your actual user credentials

        if username in valid_users and valid_users[username] == password:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Invalid username or password.")
            return False

# Пример использования
if __name__ == "__main__":
    auth_singleton = UserAuthenticationSingleton()

    # Создаем объекты стратегий
    women_strategy = WomenClothing()
    men_strategy = MenClothing()
    kids_strategy = KidsClothing()

    # Создаем объекты наблюдателя и добавляем их в магазин
    observer_1 = ClothingStoreObserver()
    observer_2 = ClothingStoreObserver()

    store = ClothingStore(women_strategy)
    store.add_observer(observer_1)
    store.add_observer(observer_2)

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if auth_singleton.authenticate_user(username, password):
            break  # Break out of the loop if authentication is successful
        else:
            print("Access denied. Authentication failed. Please try again.")

    # Определение переменных choice и store
    choice = None
    store = None

    print("Select clothing category:")
    print("1. Women")
    print("2. Men")
    print("3. Kids")
    print("4. Sport")

    choice = input("Enter category number: ")

    try:
        from factory import ClothingStrategyFactory

        # Создайте словарь скидок для каждого элемента
        item_discounts = {"Jeans": 10, "Blouse": 5, "Trousers": 15, "Shirt": 8, "Boots": 12, "Cap": 7,
                          "Running Shoes": 20, "Sport T-shirt": 10}

        clothing_strategy = ClothingStrategyFactory.create_strategy(choice)
        store = ClothingStore(clothing_strategy)
        store.set_clothing_strategy(DiscountDecorator(PriceAdapter(clothing_strategy), discounts=item_discounts))
        selected_strategy = clothing_strategy
    except ValueError as e:
        print(e)
    print("Catalog")
    for item, price_tenge, price_usd in store.get_clothing_list():
        print(f"{item}: ${price_usd:.2f} | ₸{price_tenge:.2f}")

    print("Selected category clothing:")
    for item, discounted_price, original_price in store.get_clothing_list():
        print(f"{item}: Discounted price: ${discounted_price:.2f} | Original price: ${original_price:.2f}")
