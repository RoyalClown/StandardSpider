import re

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
from Spider.Panasonic.Constant import Panasonic_Pre_Url, Third_Suffix_Url


class FirstClassUrls:
    def __init__(self, url):
        self.url = url
        html_analyse = HtmlAnalyse(url)
        self.bs_contents = html_analyse.get_bs_contents()

    def get_pages_urls(self):
        page_urls = []
        page = len(self.bs_contents.find_all(name="li", attrs={"class": "pager-item"})) + 1
        for i in range(page):
            url = self.url + "&page=" + str(i)
            page_urls.append(url)
        return page_urls

    def get_urls(self):
        urls = []
        page_urls = self.get_pages_urls()
        if page_urls is None:
            return None
        for page_url in page_urls:
            html_analyse = HtmlAnalyse(page_url)
            bs_contents = html_analyse.get_bs_contents()
            rough_urls = bs_contents.find_all(name='a', text=True, attrs={'class': 'category-box-title',
                                                                          'href': re.compile(r'/ea/products/')})
            for rough_url in rough_urls:
                url = Panasonic_Pre_Url + rough_url.get('href') + Third_Suffix_Url
                urls.append(url)
                print(url)


if __name__ == "__main__":
    firstclassurls = FirstClassUrls(
        "https://industrial.panasonic.cn/ea/products/capacitors/polymer-capacitors#quicktabs-category_page_tab=1")
    firstclassurls.get_urls()
