import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('sbc_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL,
status INTEGER NOT NULL,
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
