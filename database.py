import sqlite3

con = sqlite3.Connection('clients.db')
cur = con.cursor()

# sql = """
# CREATE TABLE users (
#     full_name VARCHAR(255) NOT NULL,
#     login VARCHAR(255) NOT NULL,
#     password VARCHAR(255) NOT NULL
# )
# """
# cur.execute(sql)
#
# sql = """
# CREATE TABLE clients (
#     account_number INTEGER PRIMARY KEY NOT NULL,
#     last_name VARCHAR(255) NOT NULL,
#     first_name VARCHAR(255) NOT NULL,
#     middle_name VARCHAR(255) NOT NULL,
#     birth_date DATE,
#     inn INTEGER(12) NOT NULL,
#     responsible_full_name VARCHAR(255) NOT NULL,
#     status VARCHAR(32) NOT NULL
# )
# """
# cur.execute(sql)

users = [
    ('Иванов Иван Иванович', 'ivanov_ii', 'ivanov_ii'),
    ('Петров Петр Петрович', 'petrov_pp', 'petrov_pp'),
    ('Сидоров Сидор Сидорович', 'sidorov_ss', 'sidorov_ss'),
    ('Кузнецов Николай Николаевич', 'kuznetsov_nn', 'kuznetsov_nn'),
    ('Смирнова Анна Алексеевна', 'smirnova_aa', 'smirnova_aa')
]

clients = [
    (1, 'Иванов', 'Иван', 'Иванович', '1985-01-10', 123456789012, 'Петров Петр Петрович', 'Не в работе'),
    (2, 'Петров', 'Петр', 'Петрович', '1978-05-15', 234567890123, 'Сидоров Сидор Сидорович', 'Не в работе'),
    (3, 'Сидоров', 'Сидор', 'Сидорович', '1990-03-20', 345678901234, 'Иванов Иван Иванович', 'Не в работе'),
    (4, 'Кузнецова', 'Ольга', 'Николаевна', '1982-07-25', 456789012345, 'Кузнецов Николай Николаевич', 'Не в работе'),
    (5, 'Смирнов', 'Алексей', 'Алексеевич', '1975-11-30', 567890123456, 'Смирнова Анна Алексеевна', 'Не в работе')
]

cur.executemany('INSERT INTO users (full_name, login, password) VALUES (?, ?, ?)', users)
cur.executemany('INSERT INTO clients (account_number, last_name, first_name, middle_name, birth_date, inn, responsible_full_name, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', clients)

con.commit()
con.close()