"""
无意义
    热对策：
        热电方式冷却辊
        半导体密封材料
        电印刷电路板材料
    工厂自动化、焊接：
        电阻焊机
    电感器：
        片式电感(批量生产终止产品)
"""

import re

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
from Spider.Panasonic.Constant import Panasonic_Pre_Url, Third_Suffix_Url


class FirstClassUrls:
    def __init__(self, urls):
        html_analyse = HtmlAnalyse(urls)
        self.bs_contents = html_analyse.get_bs_contents()

    def get_urls(self):
        urls = []
        rough_urls = self.bs_contents.find_all(name='a', text=True, attrs={'class': 'category-box-title',
                                                                           'href': re.compile(r'/ea/products/')})
        for rough_url in rough_urls:
            url = Panasonic_Pre_Url + rough_url.get('href') + Third_Suffix_Url
            urls.append(url)
            print(url)


if __name__ == "__main__":
    firstclassurls = FirstClassUrls("https://industrial.panasonic.cn/ea/products/inductors")
    firstclassurls.get_urls()
