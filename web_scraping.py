import requests
from bs4 import BeautifulSoup

search = input("Search:")
page = requests.get(f"https://www.poewiki.net/wiki/Path_of_Exile_Wiki/{search}")
soup = BeautifulSoup(page.content, "html.parser")

revise = soup.text

print(revise)