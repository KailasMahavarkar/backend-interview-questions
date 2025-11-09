from abc import ABC, abstractmethod

class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass

class Query(ABC):
    @abstractmethod
    def execute(self, sql):
        pass

class Transaction(ABC):
    @abstractmethod
    def begin(self):
        pass
    
    @abstractmethod
    def commit(self):
        pass

# ========== MYSQL FAMILY ==========
class MySQLConnection(Connection):
    def connect(self):
        return "Connected to MySQL on port 3306"

class MySQLQuery(Query):
    def execute(self, sql):
        return f"Executing MySQL query: {sql} LIMIT 100"

class MySQLTransaction(Transaction):
    def begin(self):
        return "START TRANSACTION; (MySQL)"
    
    def commit(self):
        return "COMMIT; (MySQL)"

# ========== POSTGRESQL FAMILY ==========
class PostgreSQLConnection(Connection):
    def connect(self):
        return "Connected to PostgreSQL on port 5432"

class PostgreSQLQuery(Query):
    def execute(self, sql):
        return f"Executing PostgreSQL query: {sql} FETCH FIRST 100 ROWS ONLY"

class PostgreSQLTransaction(Transaction):
    def begin(self):
        return "BEGIN; (PostgreSQL)"
    
    def commit(self):
        return "COMMIT; (PostgreSQL)"

# ========== ABSTRACT FACTORY ==========
class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self):
        pass
    
    @abstractmethod
    def create_query(self):
        pass
    
    @abstractmethod
    def create_transaction(self):
        pass

# ========== CONCRETE FACTORIES ==========
class MySQLFactory(DatabaseFactory):
    def create_connection(self):
        return MySQLConnection()
    
    def create_query(self):
        return MySQLQuery()
    
    def create_transaction(self):
        return MySQLTransaction()

class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self):
        return PostgreSQLConnection()
    
    def create_query(self):
        return PostgreSQLQuery()
    
    def create_transaction(self):
        return PostgreSQLTransaction()

# ========== CLIENT CODE ==========
class Application:
    def __init__(self, factory: DatabaseFactory):
        self.factory = factory
    
    def run(self):
        # Get all related database components
        connection = self.factory.create_connection()
        query = self.factory.create_query()
        transaction = self.factory.create_transaction()
        
        # Use them together
        print(connection.connect())
        print(transaction.begin())
        print(query.execute("SELECT * FROM users"))
        print(transaction.commit())
        print()

# ========== USAGE ==========
print("=== Running with MySQL ===")
mysql_app = Application(MySQLFactory())
mysql_app.run()

print("=== Running with PostgreSQL ===")
postgres_app = Application(PostgreSQLFactory())
postgres_app.run()
