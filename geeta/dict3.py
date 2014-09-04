import csv

f=open('file1.csv')

csv_f=csv.reader(f)

for row in csv_f:
	temp=row[2]+' '+row[3] 
	print temp

f.close()