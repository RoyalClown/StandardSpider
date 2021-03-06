"""
    @description:   
    @author:        RoyalClown
    @date:          2016/12/14
"""
from DBSave.oracleSave import OracleSave
from Spider.Panasonic.AntiPulsePowerResistors.listProducts import ProductList, Detail


def db_save(product, task_code, task_id):
    detail_attributes = Detail(product)
    component = detail_attributes.get_component(kiname="特殊功率型覆膜固定电阻器",
                                                attach="https://industrial.panasonic.cn/cdbs/www-data/pdf/RDB0000/AOA0000C279.pdf",
                                                img="https://industrial.panasonic.cn/cdbs/www-data/gif/RDB0000/AOA0000SC94.jpg")
    try:
        orcl_conn = OracleSave(task_code, task_id)
        orcl_conn.component_insert(component)

        many_properties = detail_attributes.get_properties()
        for properties in many_properties:
            orcl_conn.properties_insert(properties)
        orcl_conn.commit()
    except Exception as e:
        print(e)


def all_go(task_code, task_id,
           url="https://industrial.panasonic.cn/ea/products/resistors/fusing-resistors/fusing-resistors/anti-pulse-power-resistors?reset=1&limit=100"):
    product_list = ProductList()
    products = product_list.get_products_list(url)
    for product in products:
        db_save(product, task_code, task_id)
