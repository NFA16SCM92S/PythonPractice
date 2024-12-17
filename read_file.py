
employee_file = open("config.txt", "a") # modes: r - read, w - write , a- append
#print(employee_file.read())

employee_file.write("\nKelly  - Customer")
#print(employee_file.readline())
#for employee in employee_file.readlines():
#    print(employee)
employee_file.close()

new_file = open("inex.txt", "w")
new_file.write("THis is new file")
new_file.close()