import csv
 
with open('./data/drinks.csv', newline='') as File:  
  reader = csv.reader(File)
  myData = []
  
  for row in reader:
    zeros = []
    row[1] = row[1] if row[1].isnumeric() else 'NaN'
    row[2] = row[2] if row[2].isnumeric() else 'NaN'
    row[3] = row[3] if row[3].isnumeric() else 'NaN'

    if True:
      myData.append([row[0], row[1], row[2], row[3], row[4]])
      print(row)
 
myFile = open('./data/results.csv', 'w')
with myFile:
  writer = csv.writer(myFile)
  writer.writerows(myData)
     
print("Writing complete")
