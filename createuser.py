import sqlite3
import hashlib


def create_user(email, username, password):
    # Хеширование пароля
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Добавление нового пользователя
    c.execute('INSERT INTO users (email, password, username) VALUES (?, ?, ?)', (email, hashed_password, username))

    # Сохранение изменений и закрытие соединения с базой данных
    conn.commit()
    conn.close()
    print('Пользователь успешно создан!')


# Основная программа:
create_user(input('Введите Email пользователя: '), input('Введите имя пользователя: '), input('Введите пароль: '))
