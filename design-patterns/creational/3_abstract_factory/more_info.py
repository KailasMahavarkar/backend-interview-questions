from abc import ABC, abstractmethod

"""
    This is Abstract classes to define core features of DB
"""
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


"""
    This is DB specific concrete factories with method implementations
"""
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

    def parse(self, sql):
        return f"Parsing PostgreSQL query: {sql}"

class PostgreSQLTransaction(Transaction):
    def begin(self):
        return "BEGIN; (PostgreSQL)"
    
    def commit(self):
        return "COMMIT; (PostgreSQL)"


# ========== SIMPLE factory ==========
class SimpleDatabaseFactory:
    @staticmethod
    def create_connection(db_type):
        if db_type == "mysql":
            return MySQLConnection()
        elif db_type == "postgresql":
            return PostgreSQLConnection()
        raise ValueError(f"Unknown database: {db_type}")
    
    @staticmethod
    def create_query(db_type):
        if db_type == "mysql":
            return MySQLQuery()
        elif db_type == "postgresql":
            return PostgreSQLQuery()
        raise ValueError(f"Unknown database: {db_type}")
    
    @staticmethod
    def create_transaction(db_type):
        if db_type == "mysql":
            return MySQLTransaction()
        elif db_type == "postgresql":
            return PostgreSQLTransaction()
        raise ValueError(f"Unknown database: {db_type}")


# ========== ABSTRACT factory ==========
class AbstractDatabaseFactory(ABC):
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
class MySQLFactory(SimpleDatabaseFactory):
    def create_connection(self):
        return MySQLConnection()
    
    def create_query(self):
        return MySQLQuery()
    
    def create_transaction(self):
        return MySQLTransaction()

class PostgreSQLFactory(SimpleDatabaseFactory):
    def create_connection(self):
        return PostgreSQLConnection()
    
    def create_query(self):
        return PostgreSQLQuery()
    
    def create_transaction(self):
        return PostgreSQLTransaction()

# Usage for simple factory
connection = SimpleDatabaseFactory.create_connection("mysql")
query = SimpleDatabaseFactory.create_query("mysql")
transaction = SimpleDatabaseFactory.create_transaction("mysql")

print(connection.connect())
print(transaction.begin())
print(query.execute("SELECT * FROM users"))
print(transaction.commit())


# Usage of abstract factory
factory = MySQLFactory()
connection = factory.create_connection()
query = factory.create_query()
transaction = factory.create_transaction()

# Use them together
print(connection.connect())
print(transaction.begin())
print(query.execute("SELECT * FROM users"))
print(transaction.commit())
