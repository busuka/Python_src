import urllib.request


if __name__ == "__main__":
    url = "http://www.google.co.jp"
    r = urllib.request.urlopen(url)
    print(r.geturl())
    print(r.info())
    print(r.getcode())