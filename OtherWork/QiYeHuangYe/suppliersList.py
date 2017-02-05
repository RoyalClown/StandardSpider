import socket
import sys

from pymongo import MongoClient

from Lib.Currency.ThreadingPool import ThreadingPool
from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
from Lib.NetCrawl.Proxy_Pool import ProxyPool

sys.getdefaultencoding()
socket.setdefaulttimeout(20)

class SuppliersList:
    def __init__(self):
        self.proxy_pool = ProxyPool(flag=False)
        self.proxy_ip = self.proxy_pool.get()
        self.host = "http://www.tianyancha.com"
        conn = MongoClient()
        self.db = conn.spider


        pass

    def get_pages_urls(self):
        urls = []
        for i in range(1, 104):
            url = "http://www.soudh.com/coms-54-" + str(i) + ".html"
            urls.append(url)
        return urls

    def get_suppliers(self, url):
        html_analyse = HtmlAnalyse(url)
        bs_content = html_analyse.get_bs_contents()
        ul_tag = bs_content.find(name="div", attrs={"class": "leftbox comlist"})
        li_tags = ul_tag.find_all(name="li")
        corporations = []
        for li_tag in li_tags:
            corporation = li_tag.text.strip()
            corporation_dict = {"corporation": corporation}
            corporations.append(corporation)
            col = self.db.Company_Name
            col.insert(corporation_dict)
        print(corporations)
        return corporations

    # 企业详情页信息获取


if __name__ == "__main__":
    supplierlist = SuppliersList()
    pages_urls = supplierlist.get_pages_urls()

    threading_pool = ThreadingPool()
    threading_pool.multi_thread(supplierlist.get_suppliers, pages_urls)


