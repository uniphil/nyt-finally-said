import codecs
import sqlite3
import time
from lib.bottle import route, run, abort, template

conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE words (word text PRIMARY KEY, year integer, books integer)')

with codecs.open('./deduped.csv', encoding='utf8') as f:
    t0 = time.time()
    batch = (line.split() for line in f)
    conn.executemany('INSERT INTO words VALUES (?,?,?)', batch)
    print time.time() - t0

@route('/<word>')
def index(word):
    row = conn.execute('SELECT year, books FROM words WHERE word=?', (word,)).fetchone()
    if row is None:
        return abort(404, 'pff {word}\'s not a word'.format(word=word))
    year, books = row
    return {
        'word': word,
        'year': year,
        'books': books,
    }

run(host='localhost', port=8080)
