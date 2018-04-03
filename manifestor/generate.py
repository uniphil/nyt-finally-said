from json import load
from random import shuffle

print("manifesto:\n")

with open('manifestor/intros.json') as f:
    sentences = load(f)
    shuffle(sentences)
    print('{}\n'.format(' '.join(sentences[:3])))

with open('manifestor/bullets.json') as f:
    bullets = load(f)
    shuffle(bullets)
    for bullet in bullets[:5]:
        print("* {}".format(bullet))

with open('manifestor/conclusions.json') as f:
    sentences = load(f)
    shuffle(sentences)
    print('\n{}\n'.format(' '.join(sentences[:2])))

print("-- yael, rachel, riley, phil, 2018")
