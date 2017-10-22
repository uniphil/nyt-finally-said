import os
from lib.bottle import route, run, abort, template

@route('/<word>')
def index(word):
    if len(word) < 1:
        abort(400, 'plze provide a word to look up')

    word_with_space = '{} '.format(word)
    with open('./normalized.csv') as f:
        for line in f:
            if not line.startswith(word_with_space):
                continue
            break
        else:
            abort(404, 'pff {word}\'s not a word'.format(word=word))

    _, raw_year, raw_books = line.split(' ')
    return {
        'word': word,
        'year': int(raw_year),
        'books': int(raw_books),
    }

run(host='localhost', port=int(os.environ.get('PORT', 8080)))
