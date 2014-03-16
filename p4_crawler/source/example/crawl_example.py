# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.laenderdaten.de/bevoelkerung/geburtenrate.aspx')
soup = BeautifulSoup(r.text)

table_rows = soup.findAll("tr")
for table_data in table_rows[3:]:
	table_datas = table_data.findAll("td")
	country = table_datas[1].text
	birth_rate = table_datas[2].text
	rank = table_datas[3].text
	print country, birth_rate, rank