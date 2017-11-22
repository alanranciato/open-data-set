import json
import csv

products_parsed = json.load(open('../googler-data/products.json'))

#print(stores_parsed)

# open a file for writing

products_data = open('../googler-data/products.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(products_data)

count = 0

for prods in products_parsed:
    try:
       # print(prods.values())
        if count == 0:
            header = prods.keys()
            csvwriter.writerow(header)
            count += 1

        csvwriter.writerow(prods.values())

    except:
        print "Error on line %i", count

products_data.close()
