#!/usr/bin/env python
# -*- coding: utf-8 -*-
from babel._compat import pickle, text_type
dst_filename="../babel\localedata\zh_Hant.dat" #en.dat

with open(dst_filename, 'rb') as f:
    data = pickle.load(f)
    #data.get('_version') != version)


#print(data.get('territories'))
#print(data.get('territories_long'))

print(data.get('territories')['HK'])
print(data.get('territories')['MK'])
print(data.get('territories_long'))


dst_filename="../babel/global.dat" 
with open(dst_filename, 'rb') as f:
    data_g = pickle.load(f)

print(data_g.get('territory_containment_extra'))
print(data_g.get('territory_containment'))

#Northern America
print(data_g.get('territory_containment').get('021'))

#North America
print(data_g.get('territory_containment_extra').get('grouping').get('003'))

