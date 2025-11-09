class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self._load_from_disk()
    
    def _load_from_disk(self):
        print(f"Loading {self.filename} from disk...")
    
    def display(self):
        return f"Displaying {self.filename}"

class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None
    
    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        return self._real_image.display()

image = ProxyImage("photo.jpg")
print("Image created, but not loaded yet")
print(image.display())  # Loads now
print(image.display())  # Uses cached version