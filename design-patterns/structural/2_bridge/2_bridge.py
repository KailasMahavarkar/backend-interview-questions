from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class TV(Device):
    def turn_on(self):
        return "TV is ON"
    
    def turn_off(self):
        return "TV is OFF"

class Radio(Device):
    def turn_on(self):
        return "Radio is ON"
    
    def turn_off(self):
        return "Radio is OFF"

class RemoteControl:
    def __init__(self, device):
        self.device = device
    
    def toggle_power(self, on=True):
        if on:
            return self.device.turn_on()
        return self.device.turn_off()

tv = TV()
remote = RemoteControl(tv)
print(remote.toggle_power(True))