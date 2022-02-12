import requests

response = requests.get('http://wordleapi.azurewebsites.net/api/daily?size=5')
answer = response.text


def guess(word):
    green = []
    yellow = []
    grey = []
    for i in range(len(answer)):
        for w in word:
            if w in answer:
                if word[i] == answer[i]:
                    green.append(word[i])
                else:
                    yellow.append(w)

    for a in word:
        grey.append(a)
    grey = list(set(grey) - set(green))
    grey = list(set(grey) - set(yellow))

    print('Green = ', green, '\nYellow = ', yellow, '\nGrey = ', grey)


guess('stonk')
