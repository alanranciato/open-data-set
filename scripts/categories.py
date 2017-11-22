import json
import csv

category_parsed = json.load(open('../googler-data/categories.json'))

print(category_parsed)

# open a file for writing

category_data = open('../googler-data/categories.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(category_data)

count = 0

for cat in category_parsed:
    try:
        print(cat.values())
        if count == 0:
            header = cat.keys()
            csvwriter.writerow(header)
            count += 1

        csvwriter.writerow(cat.values())

    except:
        print "Error on line %i", count

category_data.close()
