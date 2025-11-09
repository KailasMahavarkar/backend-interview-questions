class Coffee:
    def cost(self):
        return 5
    
    def description(self):
        return "Simple coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 2
    
    def description(self):
        return self._coffee.description() + ", milk"

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 1
    
    def description(self):
        return self._coffee.description() + ", sugar"


coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
print(f"{coffee.description()} costs ${coffee.cost()}")