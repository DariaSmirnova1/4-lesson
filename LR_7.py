***Пример***
```python
cursor.execute("SELECT id, name FROM students WHERE age > 18")
rows = cursor.fetchall()
users = []
for row in rows:
	users.append(row[1])
print(users)

***Задча 1***
python
import sqlite3
conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS accounts(id INTEGER PRIMARY KEY, name TEXT NOT NULL, balance INTEGER)")
raise exception("!!!Power Failure!!!")
cursor.execute("INSERT INTO accounts(name, balance) VALUES ('Kolya', 1500)")
cursor.execute("INSERT INTO accounts(name, balance) VALUES ('Petya', 2500)")
cursor.execute("UPDATE accounts SET balance = balance - 1000 WHERE id = 1")
cursor.execute("UPDATE accounts SET balance = balance + 1000 WHERE id = 2")
conn.commit()
conn.close()

***Дополнение к задаче***
python
conn.row_factory=sqlite3.Row
cursor=conn.cursor()
cursor.execute("SELECT id, name, e-mail FROM USERS")
for row in cursor.fetchall()
print(row['name'], row['e-mail'])

***Итоговая версия с доработками :***
python
import sqlite3
#games.db
conn = sqlite3.connect("games.db")
cursor = conn.cursor()
# Создаём таблицу
cursor.execute("CREATE TABLE IF NOT EXISTS games(id INTEGER PRIMARY KEY, user_id INTEGER, score INTEGER)")
# Присоединяем users.db
cursor.execute("ATTACH DATABASE 'users.db' AS u")
cursor.execute("CREATE TABLE IF NOT EXISTS u.users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
# Данные
cursor.execute("INSERT INTO u.users(name, age) VALUES ('Kolya', 20)")
cursor.execute("INSERT INTO u.users(name, age) VALUES ('Petya', 21)")
cursor.execute("INSERT INTO u.users(name, age) VALUES ('Ivan', 20)")
cursor.execute("INSERT INTO u.users(name, age) VALUES ('Nikolai', 22)")
cursor.execute("INSERT INTO u.users(name, age) VALUES ('Sergey', 19)")
cursor.execute("INSERT INTO games(user_id, score) VALUES (4, 100500)")
cursor.execute("INSERT INTO games(user_id, score) VALUES (2, 1000)")
cursor.execute("INSERT INTO games(user_id, score) VALUES (5, 5000)")
cursor.execute("INSERT INTO games(user_id, score) VALUES (3, 10000)")
cursor.execute("INSERT INTO games(user_id, score) VALUES (3, 1000)")
cursor.execute("INSERT INTO games(user_id, score) VALUES (3, 2000)")
cursor.execute("INSERT INTO games(user_id, score) VALUES (3, 3000)")

# Join
rows = cursor.execute("""
    SELECT u.users.name, u.users.age, games.score
    FROM games
    JOIN u.users ON games.user_id = u.users.id
""").fetchall()
rows_1 = cursor.execute("""
	    SELECT games.id, name, u.user_id, age,            SUM(score) games.score
    FROM games
    LEFTJOIN u.users ON games.user_id = u.users.id
GROUP BY games.user_id
ORDER BY score""").fetchall()
print(rows)
conn.commit()
conn.close()

*** Пример следующий***
import sqlite3
conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS accounts(id INTEGER PRIMARY KEY, name TEXT, balance INTEGER)")
raise exception("!!!Power Failure!!!")
cursor.execute("INSERT INTO accounts(name, balance) VALUES ('Kolya', 1500)")
cursor.execute("INSERT INTO accounts(name, balance) VALUES ('Petya', 2500)")
cursor.execute("UPDATE accounts SET balance = balance - 1000 WHERE id = 1")
cursor.execute("UPDATE accounts SET balance = balance + 1000 WHERE id = 2")
conn.commit()
conn.close()

*** Пример 3***
import sqlite3
conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS accounts(id INTEGER PRIMARY KEY, name TEXT, balance INTEGER)")
raise exception("!!!Power Failure!!!")
cursor.execute("INSERT INTO accounts(name, balance) VALUES ('Kolya', 1500)")
cursor.execute("INSERT INTO accounts(name, balance) VALUES ('Petya', 2500)")
cursor.execute("UPDATE accounts SET balance = balance - 1000 WHERE id = 1")
cursor.execute("UPDATE accounts SET balance = balance + 1000 WHERE id = 2")
conn.commit()
conn.close()
