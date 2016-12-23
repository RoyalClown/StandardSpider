"""
    @description:   
    @author:        RoyalClown
    @date:          2016/12/2
"""
import random

import requests

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse

url = "http://www.yageo.com/NewPortal/_cn/search/productDocs.jsp?YageoPartNumber=RV0603FR-07100KL"
# html_analyse = HtmlAnalyse(url)
# content = html_analyse.get_contents()
# print(content)


res = requests.head(url, allow_redirects=False)
location = res.headers["Location"]
print(location)