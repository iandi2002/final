# observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Observable(ABC):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)
