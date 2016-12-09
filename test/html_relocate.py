"""
    @description:   
    @author:        RoyalClown
    @date:          2016/12/2
"""
from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
url = "http://www.infineon.com/cms/cn/product/power/power-mosfet/power-mosfet-bare-die/IPC313N10N3R/productType.html?productType=5546d462525dbac4015283b56e8a1cc3"
html_analyse = HtmlAnalyse(url)
bs_content = html_analyse.get_bs_contents()
trs = bs_content.find_all(name="tr", attrs={"class": "table-header gradient checker-dotted"})
for tr in trs:
    if tr.th:
        tr.th.text.strip()
    elif tr.td:
        if "DS (on)" in tr.td.text:
            print(tr.td.next_sibling.next_sibling.text.strip())
a = "a"

