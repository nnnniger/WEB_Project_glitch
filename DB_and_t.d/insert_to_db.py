import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('irondly.db')
c = conn.cursor()

# Создание таблицы, если она не существует
c.execute('''CREATE TABLE IF NOT EXISTS ossetian_words
             (iron_word TEXT, russian_word TEXT)''')

# Чтение данных из файла и запись в базу данных
with open('DB_v0.5.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.strip().split('|')
        iron_word = data[0]
        russian_word = data[1]
        c.execute("INSERT INTO ossetian_words (iron_word, russian_word) VALUES (?, ?)", (iron_word, russian_word))


conn.commit()
conn.close()
