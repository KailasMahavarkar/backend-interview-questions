class Memento:
    def __init__(self, state):
        self._state = state
    
    def get_state(self):
        return self._state

class TextEditor:
    def __init__(self):
        self._content = ""
    
    def write(self, text):
        self._content += text
    
    def get_content(self):
        return self._content
    
    def save(self):
        return Memento(self._content)
    
    def restore(self, memento):
        self._content = memento.get_state()

class History:
    def __init__(self):
        self._mementos = []
    
    def push(self, memento):
        self._mementos.append(memento)
    
    def pop(self):
        return self._mementos.pop() if self._mementos else None

# Usage
editor = TextEditor()
history = History()

editor.write("Hello ")
history.push(editor.save())

editor.write("World!")
print(editor.get_content())  # Hello World!

editor.restore(history.pop())
print(editor.get_content())  # Hello