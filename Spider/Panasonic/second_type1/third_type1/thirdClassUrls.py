"""
包括
    电容器:https://industrial.panasonic.cn/ea/products/capacitors/.../
    电感器:https://industrial.panasonic.cn/ea/products/sensors/.../
    电池:https://industrial.panasonic.cn/ea/products/batteries/.../
    电子材料:https://industrial.panasonic.cn/ea/products/electronic-materials/.../
    ...
"""

import re

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
from Spider.Panasonic.Constant import Panasonic_Pre_Url, Third_Suffix_Url


class ThirdClassUrls:
    def __init__(self, urls):
        html_analyse = HtmlAnalyse(urls)
        self.bs_contents = html_analyse.get_bs_contents()

    def get_third_urls(self):
        urls = []
        rough_urls = self.bs_contents.find_all(name='a', text=True, attrs={'class': 'category-box-title',
                                                                           'href': re.compile(r'/ea/products/')})
        for rough_url in rough_urls:
            url = Panasonic_Pre_Url + rough_url.get('href') + Third_Suffix_Url
            urls.append(url)
        return urls


if __name__ == "__main__":
    firstclassurls = ThirdClassUrls(
        "https://industrial.panasonic.cn/ea/products/input-devices/switches#quicktabs-category_page_tab=1")
    firstclassurls.get_third_urls()
