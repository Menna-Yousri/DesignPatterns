from datetime import datetime


class MyCalendar:
    def get_time(self):
        cal = datetime.now()
        day_of_week = cal.weekday()  # Monday is 0 and Sunday is 6
        return day_of_week


class Alarm:
    def __init__(self , my_calendar , my_coffee_machine):

        self.my_calendar = my_calendar
        self.my_coffee_machine = my_coffee_machine

    def snooze(self):
        day = self.my_calendar.get_time()
        if day != 5 and day != 6:  # Assuming Monday is 0 and Sunday is 6
            self.my_coffee_machine.start()

    def ring(self):
        print("RINGGG..")


class CoffeeMachine:
    def __init__(self , moving_robot , my_calendar):
        self.moving_robot = moving_robot
        self.my_calendar = my_calendar

    def start(self):
        print("Preparing Coffee")
        print("Finished Preparing Coffee")
        day = self.my_calendar.get_time()
        if day == 2:  # Assuming Wednesday is 2
            print("Adding Sugar!")
        self.moving_robot.transport()


class MovingRobot:
    def __init__(self , alarm=None , smart_window=None):
        if smart_window is None:
            pass
        else:
            self.alarm = alarm
            self.smart_window= smart_window

    def transport(self):
        print("Robot Transporting!")
        print("Reached Destination!")
        self.alarm.ring()
        if self.smart_window:
            self.smart_window.open()


class SmartWindow:
    def open(self):
        print("Opening Window")

    def close(self):
        print("Closing Window")


class MediatorTester:
    @staticmethod
    def main():
        c = MyCalendar()
        window = SmartWindow()
        mr = MovingRobot()
        cm = CoffeeMachine(mr , c)
        alarm = Alarm(c , cm)
        mr.alarm = alarm
        mr.smart_window= window
        alarm.snooze()


if __name__ == "__main__":
    MediatorTester.main()

