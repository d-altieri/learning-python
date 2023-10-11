import requests
from bs4 import BeautifulSoup


search = 'Orb of Chance' #input("Search:")
page = requests.get(f"https://www.poewiki.net/wiki/{search}")
soup = BeautifulSoup(page.content, "html.parser")


find = soup.body

title = soup.head.title.text
info_base = soup.body.p.get_text("\n")
ul_li_text = soup.body.ul


#print(title)
#print(info_base)

print(ul_li_text)