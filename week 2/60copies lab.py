"""
program which total wholesale cost for 60 copies
Author: ME
"""
import math
bookprice = 24.95
discount =0.4
shippingcostfirst=0.75
shipping_cost = 3
totalUnit=60
discountbookprice = bookprice *discount
unit_price = bookprice - discountbookprice
shipping= shipping_cost * 59 + shippingcostfirst 
result = discountbookprice + shipping
print("total price of bookprice", discountbookprice)
