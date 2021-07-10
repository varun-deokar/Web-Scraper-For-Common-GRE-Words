import requests
from bs4 import BeautifulSoup

url = "https://www.prepscholar.com/gre/blog/gre-vocabulary-list-words/"

response = requests.get(url)
# print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
# print(html_soup)

first_word = html_soup.find_all("tr")

words = []
for i in first_word:
    words.append(i.find_all("td"))

for i in words[:len(words)]:
    print(i[0].text + " - " + i[1].text)

with open("gre_vocab_words.txt", "a") as gre:
    for i in words[:len(words)]:
        gre.write(i[0].text + " - " + i[1].text + "\n")