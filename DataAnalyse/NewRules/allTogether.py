from DataAnalyse.NewRules.autoRules import DataProcessing
from DataAnalyse.NewRules.img_download import ImgDownload
from DataAnalyse.NewRules.pdf_download import PdfDownload


def all_together():
    task_code = input("请输入任务号：\n")
    while True:
        choice = input("请选择：1.下载pdf，2.下载图片，3.解析入库， 0.退出\n")
        if choice == '1':
            try:
                pdfdownload = PdfDownload(task_code)
                pdfdownload.thread_go()
                print("--------------------任务完成-------------------------")

            except Exception as e:
                print("出错，请重试", e)

        elif choice == '2':
            try:
                imgdownload = ImgDownload(task_code)
                imgdownload.thread_go()
                print("--------------------任务完成-------------------------")

            except Exception as e:
                print("出错，请重试", e)

        elif choice == '3':
            try:
                dataprocessing = DataProcessing(task_code)
                dataprocessing.go()
                print("--------------------任务完成-------------------------")
                break
            except Exception as e:
                print("出错，请重试", e)


        elif choice == '0':
            break

        else:
            print("选择出错，请重新输入")


if __name__ == "__main__":
    all_together()
