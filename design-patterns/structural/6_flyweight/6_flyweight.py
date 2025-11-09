class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        return f"Drawing {self.color} {self.name} at ({x}, {y})"


class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]


class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        return self.tree_type.draw(self.x, self.y)


oak_type = TreeFactory.get_tree_type("Oak", "Green", "Rough")
tree1 = Tree(10, 20, oak_type)
tree2 = Tree(30, 40, oak_type)
print(tree1.draw())
