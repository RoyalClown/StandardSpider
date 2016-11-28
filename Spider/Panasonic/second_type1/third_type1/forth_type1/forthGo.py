from Lib.Currency.ThreadingPool import ThreadingPool
from Lib.DBConnection.OracleConnection import OracleConnection
from Spider.Panasonic.second_type1.third_type1.forth_type1.fifth_type1.fifthGo import fifth_go
from Spider.Panasonic.second_type1.third_type1.forth_type1.forthClassUrls import ForthClassUrls


def forth_go(url, task_code, task_id):
    forth_class_urls = ForthClassUrls(url)
    fifth_urls = forth_class_urls.get_forth_urls()

    for fifth_url in fifth_urls:
        fifth_go(fifth_url, task_code, task_id)


if __name__ == "__main__":
    forth_go(
        "https://industrial.panasonic.cn/ea/products/capacitors/polymer-capacitors/os-con#quicktabs-line_up_page_tab=1",
        "CCT2016110400000000", 100)
