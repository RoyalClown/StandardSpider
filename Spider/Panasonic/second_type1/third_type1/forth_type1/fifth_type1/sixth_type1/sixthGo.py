"""
    适用https://industrial.panasonic.cn/ea/products/capacitors/polymer-capacitors/sp-cap/.../...
"""
from Spider.Panasonic.second_type1.third_type1.forth_type1.DBSave.oracleSave import OracleSave
from Spider.Panasonic.second_type1.third_type1.forth_type1.fifth_type1.sixth_type1.sixthClassUrls import SixthClassUrls


def sixth_go(url, task_code, task_id):
    sixth_class_urls = SixthClassUrls(url)
    component = sixth_class_urls.get_component()
    try:
        orcl_conn = OracleSave(task_code, task_id)
        orcl_conn.component_insert(component)

        many_properties = sixth_class_urls.get_properties()
        for properties in many_properties:
            orcl_conn.properties_insert(properties)
        orcl_conn.commit()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    sixth_go("https://industrial.panasonic.cn/ea/products/capacitors/polymer-capacitors/os-con/svpf/50SVPF68M")
