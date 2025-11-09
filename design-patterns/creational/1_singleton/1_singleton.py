class Singleton:
    _instance = None  # This is like a "box" that starts empty

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # -> create new instance
        return cls._instance


# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - same instance
