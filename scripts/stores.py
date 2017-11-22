import json
import csv

stores_parsed = json.load(open('../googler-data/stores.json'))

print(stores_parsed)

# open a file for writing

stores_data = open('../googler-data/stores.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(stores_data)

count = 0

for st in stores_parsed:
    try:
        print(st.values())
        if count == 0:
            header = st.keys()
            csvwriter.writerow(header)
            count += 1

        csvwriter.writerow(st.values())

    except:
        print "Error on line %i", count

store_data.close()
