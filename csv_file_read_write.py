import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")

# open output file
outfile = open("customer_country.csv", "w")


for record in customer_file:
    outfile.write(record[1] + "," + record[2] + "," + record[4] + "\n")

outfile.close()
