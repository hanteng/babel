#!/usr/bin/env python
# -*- coding: utf-8 -*-
from babel._compat import pickle, text_type
dst_filename="zh_Hant.dat"

with open(dst_filename, 'rb') as f:
    data = pickle.load(f)
    #data.get('_version') != version)

print(data.get('territories')['HK'])
