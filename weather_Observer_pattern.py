class ISubject:
    def register_observer(self, o):
        pass

    def remove_observer(self, o):
        pass

    def notify_observers(self):
        pass


class IDisplayElement:
    def display(self):
        pass


class WeatherData(ISubject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        if o in self.observers:
            self.observers.remove(o)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay:
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current Conditions")
        print("  Temperature:", self.temperature)
        print("  Humidity:", self.humidity)


class PhoneDisplay:
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.weather_data = weather_data
        #self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Phone Display")
        print("  Temperature:", self.temperature)
        print("  Humidity:", self.humidity)


weather_station = WeatherData()
phone_display = PhoneDisplay(weather_station)
weather_station.register_observer(phone_display)
current_conditions_display= CurrentConditionsDisplay(weather_station)
weather_station.set_measurements(25, 15, 1)