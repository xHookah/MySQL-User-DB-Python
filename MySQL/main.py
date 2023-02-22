import mysql.connector, hashlib

class MySQL_create:
    def __init__(self) -> None:
        return None
    
    def database(self):
        mydb = mysql.connector.connect(
            host='localhost', user='root'
        )

        curr = mydb.cursor()
        curr.execute("CREATE DATABASE accounts")
        curr.execute("USE accounts")
        curr.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER AUTO_INCREMENT PRIMARY KEY, email CHAR(255) NOT NULL, username CHAR(255) NOT NULL, password CHAR(255) NOT NULL)''')
        mydb.commit()
        print("Database-Table [accounts-users] has been created successfully.")

class MySQL_Connect:
    def __init__(self, email: str, username: str, password: str):
        self.email = email
        self.username = username
        self.password = password

    def connection(self):
        mydb = mysql.connector.connect(
            host='localhost', user='root', database='accounts'
        )

        curr = mydb.cursor()

        email = hashlib.sha256(self.email.encode()).hexdigest()
        username = self.username
        password = hashlib.sha256(self.password.encode()).hexdigest()

        curr.execute("INSERT INTO users (email, username, password) VALUES (%s,%s,%s)", (email, username, password))
        mydb.commit()
        print("Account has been successfully added.")


if __name__ == '__main__':

    a = int(input("[1] - Create MySQL Database | [2] - Connect and upload data to the database : "))

    match a:
        case 1:
            MySQL_create().database()
        case 2:
            email = input("Email: ")
            username = input("Username: ")
            password = input("Password: ")
            MySQL_Connect(email, username, password).connection()