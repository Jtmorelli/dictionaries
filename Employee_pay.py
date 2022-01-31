import csv

employees = open("EmployeePay.csv", "r")

employee_file = csv.reader(employees, delimiter=",")

# to skip a line if the file contains a header record
next(employee_file)

for record in employee_file:

    Salary = int(record[3])
    Bonus = float(record[4])
    Bonustotal = Salary * Bonus
    Totalsalary = Salary + Bonustotal

    print(record)
    print("ID:", record[0])
    print("First Name:", record[1])
    print("Last Name:", record[2])
    print("Base Pay:", Salary)
    print("Bonus:", float(Bonustotal))
    print("Total Pay:", float(Totalsalary))

    input()
