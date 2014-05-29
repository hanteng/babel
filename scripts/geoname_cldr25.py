#!/usr/bin/env python
# -*- coding: utf-8 -*-
#歧視無邊，回頭是岸。鍵起鍵落，情真情幻。
# url_target="https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv"

import csv
import pandas as pd
import codecs

def export_to_csv(df, ex_filename, sep=','):
    if sep==',':
        df.to_csv(ex_filename, sep=sep, quoting=csv.QUOTE_ALL, na_rep='{na}', encoding='utf-8')  #+'.csv'
    if sep=='\t':
        df.to_csv(ex_filename, sep=sep, quoting=csv.QUOTE_NONE, na_rep='{na}', encoding='utf-8')  #+'.tsv'  , escapechar="'", quotechar=""

def import_from_babel_cldr():
    from babel import Locale
    #staring from the en-US to retrieve keys
    locale = Locale('en', 'US')
    completelist_territories = locale.territories.keys()
    completelist_languages   = locale.languages.keys()
    #intiate the output dataframe from this
    df_cldr=pd.DataFrame.from_dict(locale.territories, orient="index")
    df_cldr.index.name='geocode'
    df_cldr.columns = ['name_en']
    df_cldr.sort_index(inplace=True)
    
    for i_lang in completelist_languages:
        #print i_lang
        try:
            locale = Locale.parse(i_lang)
            df=pd.DataFrame.from_dict(locale.territories, orient="index")
            df.columns = ['name_{0}'.format(i_lang)]
            df.sort_index(inplace=True)
            df_cldr=df_cldr.join(df)
        except:
            pass
    return df_cldr




######################       MAIN  ########################
import os
path_script=os.path.dirname(os.path.abspath(__file__))
#print path_script
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Fetch and generate the country and territory names in languages that are supported by the Unicode CLDR 25.""")
    parser.add_argument("-o", "--output", dest="outputpath", default="geoname_CLDR25_babel.csv",
                        help="write data to a csv file or a tsv file", metavar="OUTPUTPATH")

    args = parser.parse_args()
    
    fn = args.outputpath
    #print fn

    df_cldr=import_from_babel_cldr()
    if fn[-3:]=='csv':
        print "Outputing to",fn
        export_to_csv(df_cldr, ex_filename=os.path.join(path_script, fn), sep=',')
    elif fn[-3:]=='tsv':
        print "Outputing to",fn
        export_to_csv(df_cldr, ex_filename=os.path.join(path_script, fn), sep='\t')
    else:
        print "Only csv and tsv formats can be generated. Sorry."


    
