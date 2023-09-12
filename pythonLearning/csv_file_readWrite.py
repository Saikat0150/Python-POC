import csv


data = [

['Name', 'Age', 'City'],

['John', '25', 'New York'],

['Alice', '30', 'London'],

['Bob', '35', 'Paris']

]
with open('data.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('data.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(', '.join(row))
