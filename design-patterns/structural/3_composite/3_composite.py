from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name
    
    def operation(self):
        return self.name

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def operation(self):
        results = [self.name]
        for child in self.children:
            results.append(child.operation())
        return results

# Usage - File system example
root = Composite("root")
root.add(Leaf("file1.txt"))
folder1 = Composite("folder1")
folder1.add(Leaf("file2.txt"))
root.add(folder1)
print(root.operation())