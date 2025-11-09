from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

class ChatRoom(Mediator):
    def __init__(self):
        self.users = []
    
    def register_user(self, user):
        self.users.append(user)
    
    def notify(self, sender, message):
        for user in self.users:
            if user != sender:
                user.receive(message)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
    
    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.notify(self, message)
    
    def receive(self, message):
        print(f"{self.name} received: {message}")


# in simple terms we avoid mesh topology and create single point mediator like star topology
chat_room = ChatRoom()
user1 = User("Alice", chat_room)
user2 = User("Bob", chat_room)
chat_room.register_user(user1)
chat_room.register_user(user2)
user1.send("Hello!")