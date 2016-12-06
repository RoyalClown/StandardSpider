"""
    @description:   
    @author:        RoyalClown
    @date:          2016/11/21
"""
import requests

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse

form = {'pagecnt': 1, 'maxrows': 20, 'topage': 2, 'VAL_3_3286': '', 'VAL_3_3433': '', 'VAL_3_3287': '',
        'VAL_3_3436': '', 'part_no': ''}
session = requests.session()
session.headers.update({
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'device.panasonic.cn',
    'Origin': 'http://device.panasonic.cn',
    'Referer': 'http://device.panasonic.cn/ac/c/control/sensor/human/wl/number/index.jsp?c=search',
    'Upgrade-Insecure-Requests': '1'
})
url = "http://device.panasonic.cn/ac/c/control/sensor/human/wl/number/index.jsp?c=move"
url2 = "http://device.panasonic.cn/ac/c/control/sensor/human/wl/number/index.jsp?c=search"
session.get(url2)
content = session.post(url, data=form).text
print(content)
