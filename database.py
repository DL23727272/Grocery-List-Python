import uuid
import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="grocery_app"
        )
        self.cursor = self.connection.cursor()

    def add_todo(self, value):
        todo_id = str(uuid.uuid4())
        query = "INSERT INTO to_buy (id, value) VALUES (%s, %s)"
        self.cursor.execute(query, (todo_id, value))
        self.connection.commit()
        return todo_id

    def update_todo(self, todo_id, new_value):
        query = "UPDATE to_buy SET value = %s WHERE id = %s"
        self.cursor.execute(query, (new_value, todo_id))
        self.connection.commit()

    def delete_todo(self, todo_id):
        query = "DELETE FROM to_buy WHERE id = %s"
        self.cursor.execute(query, (todo_id,))
        self.connection.commit()

    def get_all_todos(self):
        query = "SELECT * FROM to_buy"
        self.cursor.execute(query)
        todos = []
        for row in self.cursor.fetchall():
            todos.append({"id": row[0], "value": row[1]})
        return todos

