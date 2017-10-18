import os
import codecs
import sqlite3
from lib.bottle import route, run, abort, template

conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE words (word text PRIMARY KEY, year integer, books integer)')

with codecs.open('./deduped.csv', encoding='utf8') as f:
    conn.executemany('INSERT INTO words VALUES (?,?,?)',
        (line.split() for line in f))

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

run(host='localhost', port=int(os.environ.get('PORT', 8080)))
