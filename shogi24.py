import re, sys, os, time
import urllib
import http
import http.cookiejar
import html.parser


class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        self.links = []
        self.anchor = None
        html.parser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.anchor = dict(attrs)["href"]

    def handle_data(self, data):
        if self.anchor:
            self.links.append((data, self.anchor))

    def handle_endtag(self, tag):
        if tag == "a":
            self.anchor = None


class KifuFetcher:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.cj = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))

    def login(self):
        url = "http://web.shogidojo.net/kifu/srv/login"
        params = urllib.parse.urlencode({"name": self.name, "pwd": self.pwd})
        res = self.opener.open("%s?%s" % (url, params))
        #print(res.status, res.reason)
        data = res.read()

    def search(self):
        url = "http://web.shogidojo.net/kifu/srv/search"
        one_day = 24 * 60 * 60
        from_date = time.strftime("%Y-%m-%d", time.localtime(time.time() - 90 * one_day))
        to_date = time.strftime("%Y-%m-%d", time.localtime(time.time() + one_day))
        params = urllib.parse.urlencode({"from_date": from_date, "to_date": to_date, "linkchar": "on", "submit": "検索"})
        res = self.opener.open("%s?%s" % (url, params))
        #print(res.status, res.reason)
        data = res.read()
        #print(data.decode(encoding="utf-8"))
        parser = MyHTMLParser()
        parser.feed(data.decode(encoding="utf-8"))
        return parser.links

    def get(self, url):
        res = self.opener.open(url)
        # print(url, res.status, res.reason)
        data = res.read()
        return data.decode(encoding="shift-jis")


def main(name, pwd, save_dir="kifu"):
    kf = KifuFetcher(name, pwd)
    kf.login()
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for i, (id, url) in enumerate(kf.search()):
        path = "%s/%s.kif" % (save_dir, id)
        if os.path.exists(path):
            print("skip %s %s" % (id, url))
        else:
            data = kf.get(url)
            with open(path, "w") as f:
                f.write(data)
            print("ok %s %s" % (id, url))
            time.sleep(1)


main("my_username", "password")
