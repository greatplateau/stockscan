import csv
import sys

def convert_float(str):
  if 'N/A' in str:
    return 0
  else:
    return float(str)

all_data_file = 'all_data.csv'
data_filtered = 'data_filtered.csv'

ifile  = open(all_data_file, "rb")
reader = csv.reader(ifile)
ofile  = open(data_filtered, "wb")
writer = csv.writer(ofile, delimiter=',')
header = ['Code','MC','Float Shares','Book Value','Last Trade Price','Last Trade Side','Change','Change in %','Open','Day High','Day Low','Volume','Average Daily Volume','Previous Close','52-Wk High','52-Wk Low','Change from 52-WK High','Change from 52-WK Low','% Change from 52-WK High','% Change from 52-WK Low','EPS','EBITDA','PE','PEG','50 MA','200 MA','Change from 200MA','% Change from 200 MA','Change from 50 MA','% Change from 50 MA']
writer.writerow(header)

for row in reader:
    market_cap = row[1]

    if not 'N/A' in market_cap:
     if 'M' in market_cap:
      mc = float(market_cap[:-1]) * 1000000
     elif 'B' in market_cap:
      mc = float(market_cap[:-1]) * 1000000000
     else:
      mc = float(market_cap)

     change = convert_float(row[6])
     volume = int(row[11])
     avg_volume = row[12]
     if 'N/A' in avg_volume:
      avg_volume = volume
     else:
      avg_volume = convert_float(avg_volume)
     
     high = convert_float(row[9])
     low = convert_float(row[10])
     price = convert_float(row[4])

     rough_value = (high + low)/2*volume

     ma_50 = convert_float(row[24])
     ma_200 = convert_float(row[25])

     if mc <= 30000000 and change > 0 and volume > avg_volume and rough_value > mc*0.05 and price > ma_50 and price > ma_200:
      writer.writerow(row)

ifile.close()
ofile.close()


