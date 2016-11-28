from Spider.Panasonic.second_type1.third_type1.forth_type1.fifth_type1.fifthGo import fifth_go
from Spider.Panasonic.second_type1.third_type1.forth_type1.forthClassUrls import ForthClassUrls


def forth_go(url):
    forth_class_urls = ForthClassUrls(url)
    fifth_urls = forth_class_urls.get_forth_urls()
    i = 0
    for fifth_url in fifth_urls:
        i += 1
        fifth_go(fifth_url)

    # threading_pool = ThreadingPool()
    # threading_pool.multi_thread(fifth_go, fifth_urls)


if __name__ == "__main__":
    forth_go(
        "https://industrial.panasonic.cn/ea/products/capacitors/aluminum-capacitors/aluminum-cap-smd#quicktabs-line_up_page_tab=1")
