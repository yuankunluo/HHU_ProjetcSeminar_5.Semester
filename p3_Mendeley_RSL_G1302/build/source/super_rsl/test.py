# -*- coding: utf-8 -*-

# import pprint function to make print better
from pprint import pprint
# from mendeley_client module in mendeley package import everything 
from mendeley.mendeley_client import *

# get a instance of mendeley client useing our oauth token
mendeley = create_client('rsl_config.json')
# get another instance for alternativ use
mendeley2 = create_client('rsl_config_2.json')
print(mendeley)
print(mendeley2)
