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
    download("http://device.panasonic.cn/ac/c_download/control/relay/photomos/catalog/semi_cn_rf4a_aqs22_fs_cr10.pdf?via=ok")