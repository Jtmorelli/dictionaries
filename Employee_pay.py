import csv

employees = open("EmployeePay.csv", "r")

employee_file = csv.reader(employees, delimiter=",")

# to skip a line if the file contains a header record
next(employee_file)

for record in employee_file:
    print(record)
    print("ID:", record[0])
    print("First Name:", record[1])
    print("Last Name:", record[2])
    print("Base Pay:", record[3])
    print("Bonus:", (record[3] * record[4]))
    print("Total Pay:", record[3] + (record[3] * record[4]))

    input()
