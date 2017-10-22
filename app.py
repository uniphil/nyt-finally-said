import os
from lib.bottle import route, run, abort, template
import lookup

@route('/<word>')
def index(word):
    try:
        year, books = lookup.lookup(word)
    except lookup.BadCall:
        abort(400, 'plze provide a word to look up')
    except lookup.NotFound:
        abort(404, 'pff {word}\'s not a word'.format(word=word))
    return {
        'word': word,
        'year': year,
        'books': books,
    }

run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
