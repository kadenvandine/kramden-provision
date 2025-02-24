class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, property_name):
        for observer in self._observers:
            observer.update(property_name)


class ObservableProperty:
    def __init__(self, initial_value=None):
        self._value = initial_value
        self._observers = []

    def set_value(self, new_value):
        print("ObservableProperty:set_value " + str(new_value))
        if new_value != self._value:
            self._value = new_value
            self.notify_observers()

    def get_value(self):
        print("ObservableProperty:get_value " + str(self._value))
        return self._value

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, observable):
        raise NotImplementedError("Subclass must implement the update method")

class StateObserver(Observer):
    def update(self, observable):
        print(f"Property changed to {observable.get_value()}")
