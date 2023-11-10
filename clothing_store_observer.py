#clothing_store_observer.py
from observer import Observer

class ClothingStoreObserver(Observer):
    def update(self, message):
        print(f"Notification: {message}")
