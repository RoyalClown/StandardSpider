import re

from Lib.NetCrawl.HtmlAnalyse import HtmlAnalyse
from Spider.Panasonic.Constant import Panasonic_Pre_Url, Brand_Name, B2c_Brid


class SixthClassUrls:
    def __init__(self, url):
        self.url = url
        html_analyse = HtmlAnalyse(self.url)
        self.bs_content = html_analyse.get_bs_contents()

    def get_component(self):
        # cc_url
        url = self.url

        # cc_code
        code = self.bs_content.find(name='span', attrs={'id': "model-info-model-number"}).text.replace('.', ' ')[3:]
        # cc_kiname
        kiname = self.bs_content.find(name='span', attrs={'id': "model-info-series-type"}).text.replace('.', ' ')[3:]

        rough_img = self.bs_content.find(name='img', attrs={'typeof': 'foaf:Image'}).get('src')
        # cc_img
        img = Panasonic_Pre_Url + rough_img

        rough_attach = self.bs_content.find(name='a', text=re.compile(r'产品样本')).get('href')
        # cc_attach
        attach = Panasonic_Pre_Url + rough_attach

        component = [url, code, kiname, img, attach]
        return component

    def get_properties(self):
        many_properties = []
        lists = self.bs_content.find(name='table', attrs={'class': 'spec-table'}).tbody.find_all(name='tr')

        for tr_tag in lists:
            key_value = tr_tag.find_all(name='td')
            propertyname = key_value[0].text.replace('.', ' ')
            value = key_value[1].text
            properties = [propertyname, value]
            many_properties.append(properties)
        return many_properties

if __name__ == "__main__":
    productattributes = SixthClassUrls(
        "https://industrial.panasonic.cn/ea/products/capacitors/polymer-capacitors/sp-cap/csctcx/EEFCS0G121P")
    attris = productattributes.get_component()
    print(attris)
