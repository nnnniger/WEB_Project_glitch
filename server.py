import random
import sqlite3

from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# db = SQLAlchemy(app)
count_of_words_entered = 0
attemps = 7
entered_words = []


conn = sqlite3.connect('irondly2.db')
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM ossetian_words")
count = cur.fetchone()[0]
random_id = random.randint(1, count)
cur.execute("SELECT iron_word, russian_word FROM ossetian_words WHERE id=?", (random_id,))
row = cur.fetchone()



word = row[0]
translate = row[1]
print(f"Iron word: {word}, Russian word: {translate}")


cur.close()
conn.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<int:letters>', methods=['GET', 'POST'])
def game(letters):
    global count_of_words_entered
    global entered_words
    global attemps
    if request.method == 'POST':
        word = request.form['word']
        if len(word) == letters:
            entered_words.append(word)
            print(word)
            print(count_of_words_entered)
            print(entered_words)
            count_of_words_entered += 1
            attemps -= 1
        return render_template('game.html', letters=letters, word=word, entered_words=entered_words, count_of_words_entered=count_of_words_entered, attemps=attemps)

    return render_template('game.html', letters=letters, word='еще нет слова', attemps=attemps)

if __name__ == '__main__':
    app.run(debug=True)
