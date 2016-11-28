import re


from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
from Spider.Panasonic.Constant import Panasonic_Pre_Url, Third_Suffix_Url


class ForthClassUrls:
    def __init__(self, url):
        self.url = url

    def get_pages_urls(self):
        html_analyse = HtmlAnalyse(self.url)
        bs_contents = html_analyse.get_bs_contents()
        page_urls = []
        page = len(bs_contents.find_all(name="li", attrs={"class": "pager-item"})) + 1
        for i in range(page):
            url = self.url.split('#')[0] + "?page=" + str(i) + Third_Suffix_Url
            page_urls.append(url)
        return page_urls

    def get_forth_urls(self):
        series_urls = []
        page_urls = self.get_pages_urls()
        if page_urls is None:
            return None
        for page_url in page_urls:
            html_analyse = HtmlAnalyse(page_url)
            bs_contents = html_analyse.get_bs_contents()
            tags = bs_contents.find_all(name='tr', attrs={"class": re.compile(u"ecatalog-series-table")})
            for tag in tags:
                try:
                    href = tag.find_all(name="td")[0].a.get("href")
                    m_url = Panasonic_Pre_Url + href + '&limit=100'
                    series_urls.append(m_url)
                except Exception as e:
                    href = tag.find_all(name="td")[1].a.get("href")
                    m_url = Panasonic_Pre_Url + href + '&limit=100'
                    series_urls.append(m_url)

        return series_urls


if __name__ == "__main__":
    getseries = ForthClassUrls(
        "https://industrial.panasonic.cn/ea/products/capacitors/polymer-capacitors/sp-cap#quicktabs-line_up_page_tab=1")
    seriesurls = getseries.get_forth_urls()
    print(seriesurls)
