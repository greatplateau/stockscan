from os import listdir

#combine several quote_x.csv together so we get data for all codes
quote_files = [f for f in listdir('.') if 'quote' in f]
with open('all_data.csv', 'w') as outfile:
    for fname in quote_files:
        with open(fname) as infile:
            outfile.write(infile.read())

