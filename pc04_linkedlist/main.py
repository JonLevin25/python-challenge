import requests
import re


def get_url(nothing: int):
    return f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}'

pattern = re.compile('and the next nothing is (\d+)')
newline = '\n'


nothing = '8022'
nothings = []
file = 'nothings_1'


def save_nothings(filename, arr):
    with open(filename, 'w+') as file:
        for i in arr:
            file.write(i + '\n')

for i in range(400):
    print(f'{i}: {nothing}')
    nothings.append(nothing)
    url = get_url(nothing)
    res = requests.get(url)
    if res.status_code != 200:
        print(f'nothing ({nothing}) [idx: {i}] had status code ({res.status_code})!')
        save_nothings(file, nothings)
        exit(1)
    text = res.text
    search = re.search(pattern, text)
    match = re.match(pattern, text)

    if not search:
        print(f'match failed on text: \n\t{text}')
        save_nothings(file, nothings)
        exit(1)
    if not match:
        print(f'\nIrregular: {text}\n')

    nothing = search.group(1)
