import re

Company_Urls = ['http://www.tianyancha.com/company/18695545', 'http://www.tianyancha.com/company/26700907',
                'http://www.tianyancha.com/company/632264618', 'http://www.tianyancha.com/company/9745661',
                'http://www.tianyancha.com/company/348603041', 'http://www.tianyancha.com/company/30294773',
                'http://www.tianyancha.com/company/258890183', 'http://www.tianyancha.com/company/5439623',
                'http://www.tianyancha.com/company/2352884316', 'http://www.tianyancha.com/company/16874639',
                'http://www.tianyancha.com/company/182626309', 'http://www.tianyancha.com/company/29587755',
                'http://www.tianyancha.com/company/165436964', 'http://www.tianyancha.com/company/5226527',
                'http://www.tianyancha.com/company/546190769', 'http://www.tianyancha.com/company/393050985',
                'http://www.tianyancha.com/company/25446998', 'http://www.tianyancha.com/company/1074184',
                'http://www.tianyancha.com/company/157452', 'http://www.tianyancha.com/company/2348949757']

TianYan_Headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "www.tianyancha.com",
    "Referer": "http://www.tianyancha.com/company/2546208953",
    "Tyc-From": "normal",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.14 Safari/537.36",
}

TianYan_Cookies = {
    "TYCID": "507c54ed79f24f5b91be31d1bd5181a2",
    "tnet": "183.15.177.109",
    "RTYCID": "a52996f773e34d5d8fe33fbe77024a4e",
    "aliyungf_tc": "AQAAAOPKRSE0XgIAbbEPtxQvuOglXAKD",
    "_pk_ref.1.e431": "%5B%22%22%2C%22%22%2C1484964187%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dromo1DY68BORaXNLFXjqOpXSENEvHqYbZmUvBXrLtxHcOuwbZwzQuxOwkrWHXcLI%26wd%3D%26eqid%3D95cc0ae70004bd84000000065882afcd%22%5D",
    "_pk_id.1.e431": "c06786e5b4b69640.1484296359.19.1484965768.1484964187.",
    "_pk_ses.1.e431": "*",
    "Hm_lvt_e92c8d65d92d534b0fc290df538b4758": "1484296359,1484643485,1484959709,1484960505",
    "Hm_lpvt_e92c8d65d92d534b0fc290df538b4758": "1484965768",
    "token": "9da23b167f9f43d1951f30b5cdeb5ab0",
    "_utm": "ec8d12f880154503ad0a1e15fd076e00"
}

if __name__ == "__main__":
    import requests
    import time

    my_session = requests.session()
    my_session.headers.update(TianYan_Headers)
    res = my_session.get(
        "http://www.tianyancha.com/tongji/2546208953.json?random=" + str(round(time.time(), 3)).replace(".", ""))
    content = res.content
    random_json = eval(content)
    print(random_json)
    data_v = random_json["data"]["v"]
    print(data_v)

    token = re.match(r".*?token=(.*?);.*?", str(bytes(eval(data_v)))).group(1)
    print(token)

    TianYan_Cookies["token"] = token
    my_session.cookies.update(TianYan_Cookies)
    res = my_session.get("http://www.tianyancha.com/company/2546208953.json")
    content = res.content.decode()
    print(content)
