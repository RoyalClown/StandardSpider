"""
    @description:   
    @author:        RoyalClown
    @date:          2016/11/16
"""
from Spider.Panasonic.second_type1.third_type1.forth_type1.DBSave.oracleSave import OracleSave
from Spider.PanasonicDevice.PhotoMOS.productList import Detail, ProductList


def db_save(url, code, task_code, task_id):
    detail_attributes = Detail(url, code)
    component = detail_attributes.get_component()
    try:
        orcl_conn = OracleSave(task_code, task_id)
        orcl_conn.component_insert(component)

        many_properties = detail_attributes.get_attributes()
        for properties in many_properties:
            orcl_conn.properties_insert(properties)
        # orcl_conn.commit()
    except Exception as e:
        print(e)


def all_go(task_code, task_id):
    product_list = ProductList()
    detail_urls, detail_codes = product_list.get_product_list()

    for detail_url, detail_code in zip(detail_urls, detail_codes):
        db_save(detail_url, detail_code, task_code, task_id)
