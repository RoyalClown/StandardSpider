from Spider.Panasonic.second_type1.third_type1.forth_type1.forthGo import forth_go
from Spider.Panasonic.second_type1.third_type1.thirdClassUrls import ThirdClassUrls


def third_go(url):
    third_class_urls = ThirdClassUrls(url)
    forth_urls = third_class_urls.get_third_urls()

    for forth_url in forth_urls:
        forth_go(forth_url)


if __name__ == "__main__":
    third_go(
        "https://industrial.panasonic.cn/ea/products/capacitors/polymer-capacitors#quicktabs-category_page_tab=1")
