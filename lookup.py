class BadCall(Exception):
    pass

class NotFound(Exception):
    pass

def lookup(word):
    if len(word) < 1:
        raise BadCall()

    word_with_space = '{} '.format(word)
    with open('./normalized.csv') as f:
        for line in f:
            if not line.startswith(word_with_space):
                continue
            break
        else:
            raise NotFound()

    _, raw_year, raw_books = line.split(' ')
    return int(raw_year), int(raw_books)
