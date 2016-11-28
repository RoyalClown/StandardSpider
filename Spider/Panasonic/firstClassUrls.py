import re

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
from Spider.Panasonic.Constant import *


class FirstClassUrls:
    def __init__(self):
        html_analyse = HtmlAnalyse(Panasonic_Url)
        self.bs_contents = html_analyse.get_bs_contents()

    def get_first_urls(self):
        urls = []
        rough_urls = self.bs_contents.find_all(name='a', text=True, attrs={'class': 'category-box-title',
                                                                           'href': re.compile(r'/ea/products/')})
        for rough_url in rough_urls:
            url = Panasonic_Pre_Url + rough_url.get('href')
            urls.append(url)
            print(url)


if __name__ == "__main__":
    firstclassurls = FirstClassUrls()
    firstclassurls.get_first_urls()
