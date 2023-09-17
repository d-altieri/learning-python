import urllib3

http = urllib3.PoolManager()

resp = http.request("GET", "https://www.poewiki.net/wiki/Path_of_Exile_Wiki")
web_data = []
x = resp.data.find("div")

print(x)
