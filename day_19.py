import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")

print("Title: ", soup.title.text)
print("H1: ", soup.h1.text)

links = soup.find_all("a")
for link in links:
    print(link.get("href"))