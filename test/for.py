"""
    @description:   
    @author:        RoyalClown
    @date:          2016/11/23
"""
import re

a = "\ta\n  \n    \t  ed"
b = re.compile(r'\s').sub("", a)
print(b)