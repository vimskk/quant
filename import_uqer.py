# -*- coding: utf-8 -*-

import os

import pandas as pd

import pymysql

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, "data", "uqer")
print(data_path)

command_pre = '''mysql -uquant -p123456 -h127.0.0.1 quant --local-infile=1 -e 'load data local infile "'''

command_suffix = '''" into table uqer_stock_hs
(
  `code`,
  `biz_date`,
  `pe`,
  `pb`,
  `ps`,
  `pcf`
)' '''


for file_name in os.listdir(data_path):
    file = os.path.join(data_path, file_name)
    os.system(command_pre + file + command_suffix)


