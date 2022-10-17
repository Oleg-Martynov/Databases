import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='9819862513',
                             db='multitask_db')

# Запрос на вставку данных в таблицу БД
cursor = connection.cursor()
id = 1
fullname = 'Андрей'
phone = '+79819862513'
cursor.execute('INSERT INTO user (id, full_name, phone)'
               'VALUES (%s, %s, %s)', (id, fullname, phone))
connection.commit()
# ---
cursor = connection.cursor()
cursor.execute('SELECT * FROM user WHERE id=%s', 1)
rows = cursor.fetchone()
print(f'{rows[0]} {rows[1]} {rows[2]}')
# Запрос на получение информации из БД

# ---

# TODO: Написать функцию, которая добавляет нового пользователя
#       Если пользователь с таким id уже есть, то добавление не происходит