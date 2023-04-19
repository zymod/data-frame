import csv


ids = ('4564', '764476', '6422', '45476', '3633', '235235')


for id in ids:
	with open('ids.csv', mode='a', newline='') as file:
		writter = csv.writer(file)
		writter.writerow([id]) # required '[]' to add the whole id  not iterated elements
		print('added', id)
