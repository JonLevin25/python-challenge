import sys
import requests
from bs4 import BeautifulSoup, Comment

def _is_comment(text):
    return isinstance(text, Comment)

def scrape_all_comments(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    comments = [str(comment) for comment in soup.find_all(text=_is_comment)]
    return comments

def print_comments(url):
    comments = scrape_all_comments(url)
    print("Comments:")
    for comment in comments:
        print(comment)
        print()
