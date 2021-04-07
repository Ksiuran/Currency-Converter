import requests
import json


def get_cur(code):
    return requests.get(f"http://www.floatrates.com/daily/{code.lower()}.json")


try:
    with open("usd.json", "r") as f:
        pass
except FileNotFoundError:
    with open("usd.json", "w") as f:
        page = get_cur("usd")
        f.write(page.text)
try:
    with open("eur.json", "r") as f:
        pass
except FileNotFoundError:
    with open("eur.json", "w") as f:
        page = get_cur("eur")
        f.write(page.text)
Code1 = None
Code2 = None
Money = None
fr = True
while True:
    if fr:
        Code1 = input()
    Code2 = input()
    if Code2 == "":
        break
    Money = float(input())
    print("Checking the cache...")
    try:
        with open(f"{Code2.lower()}.json", "r") as f:
            print("Oh! It is in the cache!")
            CurDict = json.load(f)
    except FileNotFoundError:
        print("Sorry, but it is not in the cache!")
        with open(f"{Code2.lower()}.json", "w") as f:
            page = get_cur(Code2)
            f.write(page.text)
            CurDict = json.loads(page.text)
    Money = Money * CurDict[f'{Code1.lower()}']['inverseRate']
    print(f'You received {round(Money, 2)} {Code2.upper()}.')
    fr = False
