# Command interface
class Command:
    def execute(self):
        pass

    def unexecute(self):
        pass

# Concrete command for turning a device on
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device
        self.previous_state = None

    def execute(self):
        self.previous_state = self.device.get_state()
        self.device.turn_on()

    def unexecute(self):
        if self.previous_state:
            self.device.set_state(self.previous_state)

# Concrete command for turning a device off
class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device
        self.previous_state = None

    def execute(self):
        self.previous_state = self.device.get_state()
        self.device.turn_off()

    def unexecute(self):
        if self.previous_state:
            self.device.set_state(self.previous_state)

# Concrete command for adjusting the volume of a stereo
class AdjustVolumeCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
        self.previous_volume = None

    def execute(self):
        self.previous_volume = self.stereo.get_volume()
        self.stereo.adjust_volume()

    def unexecute(self):
        if self.previous_volume is not None:
            self.stereo.set_volume(self.previous_volume)

# Concrete command for changing the channel of a TV
class ChangeChannelCommand(Command):
    def __init__(self, tv):
        self.tv = tv
        self.previous_channel = None

    def execute(self):
        self.previous_channel = self.tv.get_channel()
        self.tv.change_channel()

    def unexecute(self):
        if self.previous_channel is not None:
            self.tv.set_channel(self.previous_channel)

# Receiver interface
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def get_state(self):
        pass

    def set_state(self, state):
        pass

# Concrete receiver for a TV
class TV(Device):
    def turn_on(self):
        print("TV is now on")

    def turn_off(self):
        print("TV is now off")

    def change_channel(self):
        print("Channel changed")

    def get_channel(self):
        return "Some Channel"

    def set_channel(self, channel):
        print(f"Setting channel to {channel}")

    def get_state(self):
        return self.get_channel()

    def set_state(self, state):
        self.set_channel(state)

# Concrete receiver for a stereo
class Stereo(Device):
    def turn_on(self):
        print("Stereo is now on")

    def turn_off(self):
        print("Stereo is now off")

    def adjust_volume(self):
        print("Volume adjusted")

    def get_volume(self):
        return 50

    def set_volume(self, volume):
        print(f"Setting volume to {volume}")

    def get_state(self):
        return self.get_volume()

    def set_state(self, state):
        self.set_volume(state)

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo_button(self):
        if self.command:
            self.command.unexecute()

# Example usage
if __name__ == "__main__":
    # Create devices
    tv = TV()
    stereo = Stereo()

    # Create command objects
    turn_on_tv_command = TurnOnCommand(tv)
    turn_off_tv_command = TurnOffCommand(tv)
    adjust_volume_stereo_command = AdjustVolumeCommand(stereo)
    change_channel_tv_command = ChangeChannelCommand(tv)

    # Create remote control
    remote = RemoteControl()

    # Set and execute commands
    remote.set_command(turn_on_tv_command)
    remote.press_button()  # Outputs: TV is now on

    remote.set_command(adjust_volume_stereo_command)
    remote.press_button()  # Outputs: Volume adjusted

    remote.set_command(change_channel_tv_command)
    remote.press_button()  # Outputs: Channel changed

    remote.set_command(turn_off_tv_command)
    remote.press_button()  # Outputs: TV is now off

    # Undo last command
    remote.press_undo_button()  # Outputs: TV is now on (Undo last command)
