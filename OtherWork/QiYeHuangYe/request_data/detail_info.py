import json
import re

import requests
import time

from pymongo import MongoClient

from Lib.Currency.ThreadingPool import ThreadingPool
from Lib.NetCrawl.Proxy_Pool import ProxyPool
from OtherWork.QiYeHuangYe.request_data.Constant import TianYan_Headers, TianYan_Cookies


class DetailInfo:
    def __init__(self):
        self.proxy_pool = ProxyPool()
        self.proxy_ip = self.proxy_pool.get()

    def get_detail(self, url):
        while True:
            my_session = requests.session()
            my_session.headers.update(TianYan_Headers)
            my_session.proxies.update(self.proxy_ip)
            try:
                first_res = my_session.get(url + ".json?random=" + str(
                    round(time.time(), 3)).replace(".", ""))
                first_content = first_res.content
            except Exception as e:
                print(e)
                self.proxy_pool.remove(self.proxy_ip)
                self.proxy_ip = self.proxy_pool.get()
                continue
            if first_res.status_code != 200 or not first_content:
                self.proxy_pool.remove(self.proxy_ip)
                self.proxy_ip = self.proxy_pool.get()
                continue
            first_data_v = eval(first_content)["data"]["v"]
            first_token = re.match(r".*?token=(.*?);.*?", str(bytes(eval(first_data_v)))).group(1)

            my_cookie = TianYan_Cookies

            my_cookie["token"] = first_token

            my_session.cookies.update(my_cookie)

            try:
                real_res = my_session.get(url + ".json?")

                content = real_res.content.decode()
            except Exception as e:
                print(e)
                self.proxy_pool.remove(self.proxy_ip)
                self.proxy_ip = self.proxy_pool.get()
                continue
            if first_res.status_code != 200 or not content:
                self.proxy_pool.remove(self.proxy_ip)
                self.proxy_ip = self.proxy_pool.get()
                continue
            break
        conn = MongoClient()
        json_list = json.loads(content)
        brief_companies = json_list["data"]
        col = conn.spider.Company_Info
        if not brief_companies:
            print(url, "无数据")
            col.update({"url": url}, {'$set': {"状态": "无数据"}}, multi=True)
        else:
            col.update({"url": url}, {'$set': {"data": json_list}}, multi=True)
        conn.close()

        return


if __name__ == "__main__":
    mongo_conn = MongoClient()
    col = mongo_conn.spider.Company_Info
    detail_info = DetailInfo()
    urls = []
    for data in col.find({"状态": "未完成"}):
        url = data["url"]
        urls.append(url)

    threadingpool = ThreadingPool()
    threadingpool.multi_thread(detail_info.get_detail, urls)
