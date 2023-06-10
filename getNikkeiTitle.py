import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/news/headline/archive/"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

spans = soup.find_all("span")

nikkei_headline_title = []

for span in spans:
    try:
        string_ = span.get("class").pop(0)

        if string_ in ["cmnc-middle", "cmnc-small"]:
            nikkei_headline_title.append(span.string)

    except:
        pass

for title in nikkei_headline_title:
    print (title)
