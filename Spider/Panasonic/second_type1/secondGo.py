from Spider.Panasonic.second_type1.secondClassUrls import SecondClassUrls
from Spider.Panasonic.second_type1.third_type1.thirdGo import third_go


def second_go(url):
    second_class_urls = SecondClassUrls(url)
    third_urls = second_class_urls.get_second_urls()

    for third_url in third_urls:
        third_go(third_url)


if __name__ == "__main__":
    second_go(
        "https://industrial.panasonic.cn/ea/products/capacitors")
