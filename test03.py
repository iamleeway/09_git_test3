from pandas.io.json import json_normalize
from pprint import pprint

sample_object = {'Name':'John', 'Location':{'City':'Los Angeles','State':'CA'}}
a = json_normalize(sample_object)
pprint(sample_object)
pprint(a)
