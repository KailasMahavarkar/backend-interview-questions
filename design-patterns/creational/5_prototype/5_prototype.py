import copy

class Prototype:
    def __init__(self):
        self._objects = {}
    
    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def unregister_object(self, name):
        del self._objects[name]
    
    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def __str__(self):
        return f"{self.color} {self.model}"

# Usage
prototype = Prototype()
prototype.register_object('basic_car', Car(
    model='Sedan',
    color="White"
))

car1 = prototype.clone('basic_car', color='Red')
car2 = prototype.clone('basic_car', color='Blue')
print(car1, car2)