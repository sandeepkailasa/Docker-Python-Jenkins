import csv

with open('input.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        a = int(row['a'])
        b = int(row['b'])
        result = a + b
        print(f"Sandeep's Updated Function {a} + {b} = {result}")

