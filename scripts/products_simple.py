import json
import csv

products_parsed = json.load(open('/Users/eg1169/Desktop/productdb/products.json'))

#print(stores_parsed)

# open a file for writing

products_data = open('/Users/eg1169/Desktop/productdb/products1.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(products_data)

count = 0
errCount = 0
prodName = ''

for prods in products_parsed:
    try:
      count +=1
      #print(prods.values())
      if count == 0:
        header = prods.keys()
        #csvwriter.writerow(header)

      prodName = prods['name'] or prods['description']


      #csvwriter.writerow(prods.values())
      csvwriter.writerow([[prods['sku'], prodName.encode("utf-8"),prods['url'],prods['image']]])

#print ("Count %i: %s | %s | %s | %s", count, prods['sku'], prods['name'],prods['url'],prods['image'])

      #if count > 20:
      #  break
    except Exception as e:
      print "Error Count %i: %s | %s", count, prods['sku'], prods['name']
      print "Error %s", e
      errCount += 1

print ("Count %i, Errors %i", count, errCount)

#products_data.close()
