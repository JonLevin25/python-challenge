from common.scrape_comment import scrape_all_comments
import re


PATH = '../pc03_equality/text'
def get_text(path):
    with open(path, 'r') as file:
        return file.read()

def get_urls():
    with open('../urls') as file:
        return file.read().split('\n')

if __name__ == '__main__':
    text = get_text(PATH)
    pattern = re.compile(r'(?<![A-Z])([A-Z]{3})([a-z])([A-Z]{3})[^A-Z]')
    matches = [m for m in re.finditer(pattern, text)]



    # comments = [scrape_all_comments(url) for url in get_urls()]
    #
    # print(list(zip(comments)))
    # for c in comments:
    #     print(c)

    g1 = [m.group(1) for m in matches]
    g3 = [m.group(3) for m in matches]

zip()
    zipped = zip(g1, g3)
    for z in zipped:
        print(z)