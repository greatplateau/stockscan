#/bin/bash

python download_yahoo.py
sed -i 's/\"//g' all_data.csv
sort all_data.csv > all_data_sorted.csv
python filter_data.py all_data_sorted.csv

