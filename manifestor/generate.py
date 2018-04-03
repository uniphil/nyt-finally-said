from json import load
from random import shuffle

with open('manifestor/bullets.json') as f:
    bullets = load(f)
    shuffle(bullets)
    bullets = bullets[:5]

print("manifesto:\n")

for bullet in bullets:
    print("* {}\n".format(bullet))

print("-- yael, rachel, riley, phil, 2018")
