'''
from bs4 import BeautifulSoup
import requests

r = requests.get("https://dota2.fandom.com/wiki/Heroes")
soup = BeautifulSoup(r.content, 'html.parser')
links_with_text = []
for a in soup.find_all('a', href=True):
    title = a.get('title')
    print(title)

print('Done')
'''

with open('heroes.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
