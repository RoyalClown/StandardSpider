"""
    @description:   
    @author:        RoyalClown
    @date:          2016/12/2
"""
from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
url = "https://toshiba.semicon-storage.com/info/docget.jsp?did=3263&prodName=1SS181"
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

