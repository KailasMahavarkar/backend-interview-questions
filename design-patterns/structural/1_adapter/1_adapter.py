class USASocket:
    def voltage(self):
        return 120
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
    def earth(self):
        return 0

class EuropeanSocket:
    def voltage(self):
        return 230
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
    def earth(self):
        return 0

class EuropeanToUSAAdapter:
    def __init__(self, european_socket):
        self.socket = european_socket
    
    def voltage(self):
        # Convert 230V to 120V
        return 110  # Step-down transformer
    
    def live(self):
        # Pass through from European socket
        return self.socket.live()
    
    def neutral(self):
        return self.socket.neutral()
    
    def earth(self):
        return self.socket.earth()

# CLIENT CODE: Expects USASocket interface
class ElectricKettle:
    def __init__(self, socket):
        self.socket = socket
    
    def boil(self):
        if self.socket.voltage() > 125:
            return "⚠️ Voltage too high! Kettle damaged!"
        return f"✓ Boiling water using {self.socket.voltage()}V"

# Usage
print("=== Direct USA Socket ===")
usa_socket = USASocket()
kettle1 = ElectricKettle(usa_socket)
print(kettle1.boil())

print("\n=== European Socket WITHOUT Adapter ===")
eu_socket = EuropeanSocket()
kettle2 = ElectricKettle(eu_socket)
print(kettle2.boil())  # Would damage the kettle!

print("\n=== European Socket WITH Adapter ===")
adapted_socket = EuropeanToUSAAdapter(eu_socket)
kettle3 = ElectricKettle(adapted_socket)
print(kettle3.boil())  # Safe!
