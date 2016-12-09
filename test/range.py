import random
import urllib.request

import requests

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse


def download(pdf_url):
    filename = str(random.random()) + '.pdf'
    res = requests.get(pdf_url)
    with open(filename, 'wb') as f:
        f.write(res.content)


if __name__ == "__main__":
    with open("a.txt", "w", encoding="utf-8") as f:
        f.write(r"水电费")

