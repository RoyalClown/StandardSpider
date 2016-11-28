import re

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
from Spider.Panasonic.Constant import Panasonic_Pre_Url


class FifthClassUrls:
    def __init__(self, url):
        self.url = url

    def get_pages_urls(self):
        html_analyse = HtmlAnalyse(self.url, is_proxy=True)
        bs_content = html_analyse.get_bs_contents()
        page_urls = []
        page = len(bs_content.find_all(name="li", attrs={"class": "pager-item"})) + 1
        for i in range(page):
            url = self.url + "&page=" + str(i)
            page_urls.append(url)
        return page_urls

    def get_fifth_urls(self):
        product_urls = []
        page_urls = self.get_pages_urls()
        if page_urls is None:
            return None
        for page_url in page_urls:
            html_analyse = HtmlAnalyse(page_url)
            bs_contents = html_analyse.get_bs_contents()
            lists = bs_contents.find_all(name='tr', attrs={"class": re.compile(u"ecatalog-model-table")})
            for list in lists:
                model = list.td.a
                href = model.get("href")
                url = Panasonic_Pre_Url + href
                product_urls.append(url)
        return product_urls


if __name__ == "__main__":
    get_product = FifthClassUrls(
        "https://industrial.panasonic.cn/ea/products/capacitors/polymer-capacitors/sp-cap/csctcx?reset=1")
    lists = get_product.get_fifth_urls()
    print(lists)
