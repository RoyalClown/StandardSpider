from Spider.Panasonic.second_type1.third_type1.forth_type1.fifth_type1.fifthClassUrls import FifthClassUrls
from Spider.Panasonic.second_type1.third_type1.forth_type1.fifth_type1.sixth_type1.sixthGo import sixth_go


def fifth_go(url, task_code, task_id):
    fifth_class_urls = FifthClassUrls(url)
    six_urls = fifth_class_urls.get_fifth_urls()

    # threading_pool = ThreadingPool()
    # threading_pool.multi_thread(sixth_go, sixth_urls)

    for six_url in six_urls:
        sixth_go(six_url, task_code, task_id)


if __name__ == "__main__":
    fifth_go("https://industrial.panasonic.cn/ea/products/capacitors/aluminum-capacitors/aluminum-cap-smd/hd-v-high-temp-reflow?reset=1&limit=100",
             "CCT2016110400000004", 24)
