from abc import ABC, abstractmethod

# ============================================
# STATE INTERFACE
# ============================================
class TrafficLightState(ABC):
    @abstractmethod
    def change(self, light):
        pass


# ============================================
# CONCRETE STATES
# ============================================
class RedLight(TrafficLightState):
    def change(self, light):
        print("🔴 RED - Stop! Wait for green...")
        light.state = GreenLight()  # Next state


class GreenLight(TrafficLightState):
    def change(self, light):
        print("🟢 GREEN - Go! Drive safely...")
        light.state = YellowLight()  # Next state


class YellowLight(TrafficLightState):
    def change(self, light):
        print("🟡 YELLOW - Slow down! Prepare to stop...")
        light.state = RedLight()  # Next state


# ============================================
# CONTEXT
# ============================================
class TrafficLight:
    def __init__(self):
        self.state = RedLight()  # Start with red
    
    def change(self):
        self.state.change(self)  # Delegate to current state


# Demo
light = TrafficLight()
light.change()  # RED → GREEN
light.change()  # GREEN → YELLOW
light.change()  # YELLOW → RED
light.change()  # RED → GREEN