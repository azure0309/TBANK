import bank
from bank import Connection

connection = Connection()
connect = connection.connect()
cursor = connection.cursor()

print("Welcome to the Internet bank")
print("Enter your first name:")
fname = input(">")

