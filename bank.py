import sqlite3

class Connection():
	def connect(self):
		conn = sqlite3.connect('tbank.db')
		return conn
	def cursor(self, connect = connect()):
		cur = connect.cursor()
		return cur

class User():
	def __init__(self, id, first_name, last_name, age, register_id, account_number, card_number):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.register_id = register_id
		self.account_number = account_number
		self.card_number = card_number
	def description(self):
		print(self.first_name, self.age, self.account_number)

class Model(User):
	def addUser(self):
		connection = Connection()
		cursor = connection.cursor()
		conn = connection.connect()
		query = f"insert into customer (fname, lname, account_number, card_number) values ('{self.first_name}', '{self.last_name}', '{self.account_number}', '{self.card_number}');"
		cursor.execute(query)
		conn.commit()


class Account():
	def __init__(self, id, account_number, type, status):
		self.id = id
		self.account_number = account_number
		self.type = type
		self.status = status



