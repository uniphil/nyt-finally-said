import os
import redis
import requests
from requests_oauthlib import OAuth1
import lookup

first_said = 'nyt_first_said'

auth = OAuth1(os.environ['KEY'], os.environ['SECRET'],
              os.environ['USER_TOKEN'], os.environ['USER_SECRET'])

def get_new_tweets(since):
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    url += '?screen_name={}&trim_user=1'.format(first_said)
    if since is not None:
        url += '&since_id={}'.format(since.decode('utf-8'))
    return requests.get(url, auth=auth).json()

def humanize(word, year, books):
    return '“{word}” has been published in at least {books} books since {year}'\
        .format(word=word, year=year, books=books)

def respond(word, tweet_id):
    try:
        year, books = lookup.lookup(word)
    except lookup.NotFound:
        print('google disagrees, nyt:', word)
        return
    except lookup.BadCall:
        print('wat', word)
        return
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    data = {
        'status': '@{} {}'.format(first_said, humanize(word, year, books)),
        'in_reply_to_status_id': tweet_id,
    }
    resp = requests.post(url, auth=auth, data=data)
    print('posted', data['status'], resp.ok)

if __name__ == '__main__':
    print('connecting to redis...')
    r = redis.StrictRedis.from_url(os.environ['REDIS_URL'])
    last = r.get('last')
    print('fetching tweets since {}'.format(last))
    tweets = get_new_tweets(since=last)
    print('found {}. looking them up...'.format(len(tweets)))
    for tweet in reversed(tweets):
        word, tweet_id = tweet['text'], tweet['id_str']
        respond(word, tweet_id)
        r.set('last', tweet_id)
    print('bye!')
