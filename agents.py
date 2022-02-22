import random

validwordlist = []

with open("wordlist.txt") as validwords:
    for ww in validwords:
        validwordlist.append(ww[:5])


def agent_random():
    return random.choice(validwordlist)

def game():
    agent_random()


