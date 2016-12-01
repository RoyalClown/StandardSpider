import gzip
import json
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

from Lib.NetCrawl.Constant import Default_Header
from Lib.NetCrawl.Proxy import Proxy


class HtmlAnalyse:
    def __init__(self, url, is_proxy=False, is_cookie=False):
        self.url = url
        self._session = requests.Session()
        self._session.headers.update(Default_Header)
        if is_proxy:
            proxy_ip = {'http': '113.3.72.98:8998'}
            self._session.proxies.update(proxy_ip)
        if is_cookie:
            with open("I:\\PythonPrj\\zhihu\\test.json") as f:
                cookies = f.read()
            print(cookies)
            cookies_dict = json.loads(cookies)
            self._session.cookies.update(cookies_dict)

    # 获得页面内容
    def get_contents(self):
        try:
            contents = self._session.get(self.url).text
            return contents
        except Exception as e:
            print(e)
            self.get_contents()

    # 模拟浏览器获得内容
    def get_selenium_contents(self):
        driver = webdriver.PhantomJS(
            executable_path='C:\\Users\\RoyalClown\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
        try:
            driver.get(self.url)
            contents = driver.page_source
            driver.quit()
            return contents
        except Exception as e:
            print(e)
            self.get_selenium_contents()

    # 获得bs对象
    def get_bs_contents(self):
        bs_contents = BeautifulSoup(self.get_contents(), "html.parser")
        return bs_contents

    # 模拟浏览器获得bs对象
    def get_selenium_bs_contents(self):
        bs_contents = BeautifulSoup(self.get_selenium_contents(), "html.parser")
        return bs_contents

    # 解压文本
    def explode(self):
        content = self.get_contents()
        try:  # 尝试解压
            print('正在解压.....')

            content = gzip.decompress(content)
            print('解压完毕!')
        except:
            print('未经压缩, 无需解压')
        return content

    # 下载文件
    def download(self, path):
        res = self._session.get(self.url, stream=True)
        with open(path, 'wb') as f:
            f.write(res.content)


if __name__ == "__main__":
    html_analyse = HtmlAnalyse("http://www.atmel.com/zh/cn/Images/Atmel-8700-SEEPROM-AT24C01C-02C-Datasheet.pdf")
    html_analyse.download('a.pdf')
