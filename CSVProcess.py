import csv

fo = open('DataSet.csv', 'r')
fw = open('cleanedDataSet.csv', 'wb')

csvReader = csv.reader(fo)
csvWriter = csv.writer(fw,delimiter="\v",lineterminator="\a")
count = 0                
for row in csvReader:
    count = count + 1
    csvWriter.writerow(row)
    fw.flush()
print count
fo.close()
fw.close()
