from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        return "Rendering Windows button"


class MacButton(Button):
    def render(self):
        return "Rendering Mac button"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()


factory = WindowsFactory()
button = factory.create_button()
print(button.render())


# what is the core difference?

# 2_factory_pattern
# You tell the factory WHAT to make
# factory = AnimalFactory()
# animal = factory.create_animal("dog")  # Pass the type as a string

# 3_abstract_patterm
# You choose WHICH factory to use
# factory = WindowsFactory()  # Choose the factory
# button = factory.create_button()  # Factory decides what to make
