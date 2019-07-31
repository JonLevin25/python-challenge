# import urllib.request
from collections import Counter

# URL = 'http://www.pythonchallenge.com/pc/def/ocr.html'
#
# html = str(urllib.request.urlopen(URL).read(), 'utf-8')
#
# with open('./original.html', 'w') as file:
#     file.write(html)

# get text
file = open('text')
text = file.read()
file.close()

# create counter
counter = Counter(text)
sorted_keys = [(k, counter[k]) for k in sorted(counter.keys(), key=lambda k: counter[k], reverse=True)]

for tup in sorted_keys:
    print(tup)


