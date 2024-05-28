from flask import Flask, render_template, redirect, url_for, request
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'hy78tygigh98jrt5rj241h4'  # Секретный ключ для хеширования данных сессии при авторизации


# Устанавливаем соединение с Базой Данных
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        error = None  # обнуляем переменную ошибок

        username = request.form['username']  # обрабатываем запрос с нашей формы который имеет атрибут name="username"
        password = request.form['password']  # обрабатываем запрос с нашей формы который имеет атрибут name="password"
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()  # шифруем пароль в sha-256

        # устанавливаем соединение с БД
        conn = get_db_connection()
        # создаем запрос для поиска пользователя по username,
        # если такой пользователь существует, то получаем все данные id, password
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        # закрываем подключение БД
        conn.close()

        # теперь проверяем если данные сходятся формы с данными БД
        if user and user['password'] == hashed_password:
            # в случае успеха создаем сессию в которую записываем id пользователя
            session['user_id'] = user['id']
            # и делаем переадресацию пользователя на новую страницу -> в нашу адимнку
            return redirect(url_for('control'))
        else:
            error = 'Неверное имя пользователя или пароль!'
        return render_template('index.html', error=error)

    return render_template('index.html')


@app.route('/control')
def control():
    if 'user_id' not in session:
        return redirect(url_for('/'))
    return render_template('control.html')


if __name__ == '__main__':
    app.run(debug=True)
