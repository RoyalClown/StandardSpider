"""
    @description:   
    @author:        RoyalClown
    @date:          2016/12/2
"""
from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse

html_analyse = HtmlAnalyse('http://www.vishay.com/doc?88769')
content = html_analyse.get_contents()
print(content)