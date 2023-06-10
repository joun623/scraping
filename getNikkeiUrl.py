import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/news/headline/archive/"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

a_tags = soup.find_all("a")
nikkei_news_url = []

for a_tag in a_tags:
    try:
        # if "article/DGX" in a_tag.get("href"):
        if a_tag.get("href").startswith("/article/DGX"):
            nikkei_news_url.append(a_tag.get('href'))

    except:
        pass

for url in nikkei_news_url:
    print (url)
