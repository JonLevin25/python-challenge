# import common.scrape_comment as scrape
# URL = 'http://www.pythonchallenge.com/pc/def/equality.html'
#
# comments = scrape.scrape_all_comments(URL)
# print(comments[0])
# with open('./text', 'w') as file:
#     file.write(comments[0])

import re

text = ''
with open('./text', 'r') as file:
    text = file.read()

matches = re.finditer('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text)
# for m in matches:
#     print(m)
letters = [m.group(1) for m in matches]
print(''.join(letters))