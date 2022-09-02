#Welcome message to the Customers 
print("Welcome to the Tip Calculator!")

#Converting the bill data type from string to float.
bill = float(input("What is the total bill? $"))

#Asking the user how much tip would you like to give? And converting the tip data type from string to float.
tip = float(input("How much tip would you like to give? 10, 12, or 15?"))

#Asking how many people to split the bill? and Converting the data type from string to integer
people = int(input("How many people are splitting the bill"))

#Getting the tip percentage = tip / 100
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

#Dividing the total bill by the number of people and rounding it up to 2 decimal places
bill_per_person = round(total_bill / people, 2)
print(bill_per_person)