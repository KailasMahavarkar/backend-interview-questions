from abc import ABC, abstractmethod

class SupportHandler(ABC):
    """Base support handler"""
    def __init__(self, name):
        self.name = name
        self._next_handler = None
    
    def set_next(self, handler):
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, ticket):
        if self._next_handler:
            return self._next_handler.handle(ticket)
        return f"Nobody could handle: {ticket['issue']}"


class ChatBot(SupportHandler):
    """Handles simple issues (priority 1)"""
    
    def handle(self, ticket):
        if ticket['priority'] == 1:
            return f"{self.name}: ✓ Handled '{ticket['issue']}' (simple issue)"
        print(f"{self.name}: ✗ Can't handle, escalating...")
        return super().handle(ticket)


class JuniorAgent(SupportHandler):
    """Handles medium issues (priority 2)"""
    
    def handle(self, ticket):
        if ticket['priority'] == 2:
            return f"{self.name}: ✓ Handled '{ticket['issue']}' (medium issue)"
        print(f"{self.name}: ✗ Can't handle, escalating...")
        return super().handle(ticket)


class SeniorAgent(SupportHandler):
    """Handles complex issues (priority 3)"""
    
    def handle(self, ticket):
        if ticket['priority'] == 3:
            return f"{self.name}: ✓ Handled '{ticket['issue']}' (complex issue)"
        print(f"{self.name}: ✗ Can't handle, escalating...")
        return super().handle(ticket)


# Create support chain
chatbot = ChatBot("ChatBot")
junior = JuniorAgent("Junior Agent")
senior = SeniorAgent("Senior Agent")

chatbot.set_next(junior).set_next(senior)

# Test tickets
print("Ticket 1:")
print(chatbot.handle({'issue': 'Password reset', 'priority': 1}))
print()

print("Ticket 2:")
print(chatbot.handle({'issue': 'Billing question', 'priority': 2}))
print()

print("Ticket 3:")
print(chatbot.handle({'issue': 'System outage', 'priority': 3}))
print()

print("Ticket 4:")
print(chatbot.handle({'issue': 'Unknown issue', 'priority': 999}))
