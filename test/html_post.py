"""
    @description:   
    @author:        RoyalClown
    @date:          2016/11/21
"""
import requests
form = {"page": "2", "pageSize": "30"}
res = requests.post("http://www.diodes.com/api/catalog/51/products")
print(res.content.decode("utf-8"))
