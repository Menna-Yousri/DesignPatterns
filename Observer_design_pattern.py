from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class EventManager:
    """
    The EventManager class acts as a ConcreteSubject. It notifies subscribers about events.
    """

    _observers: List[EventListener] = []

    def attach(self, observer: EventListener) -> None:
        print("EventManager: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: EventListener) -> None:
        self._observers.remove(observer)

    def notify(self, event_type: str, data: str) -> None:
        """
        Notify all observers about an event.
        """
        print(f"EventManager: Notifying observers about event '{event_type}'...")
        for observer in self._observers:
            observer.update(event_type, data)

    def open_file(self, path: str) -> None:
        """
        Simulate opening a file and notify observers.
        """
        print(f"EventManager: Opening file '{path}'...")
        self.notify("open", path)

    def save_file(self, path: str) -> None:
        """
        Simulate saving a file and notify observers.
        """
        print(f"EventManager: Saving file '{path}'...")
        self.notify("save", path)


class EventListener(ABC):
    """
    The EventListener interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, event_type: str, data: str) -> None:
        """
        Receive update from subject.
        """
        pass


class LoggingListener(EventListener):
    """
    ConcreteObserverA reacts to the 'open' event.
    """

    def update(self, event_type: str, data: str) -> None:
        if event_type == "open":
            print(f"LoggingListener: Someone has opened the file: {data}")


class EmailAlertsListener(EventListener):
    """
    ConcreteObserverB reacts to the 'save' event.
    """

    def update(self, event_type: str, data: str) -> None:
        if event_type == "save":
            print(f"EmailAlertsListener: Someone has changed the file: {data}")


if __name__ == "__main__":
    # The client code.

    event_manager = EventManager()

    logger = LoggingListener()
    event_manager.attach(logger)

    email_alerts = EmailAlertsListener()
    event_manager.attach(email_alerts)

    event_manager.open_file("/path/to/file.txt")
    event_manager.save_file("/path/to/another_file.txt")

    event_manager.detach(logger)

    event_manager.open_file("/path/to/yet_another_file.txt")
