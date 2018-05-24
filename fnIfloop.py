
# if statement in python

# if condition is true, execute the next block of code (indented)
# if condition is false, skip the block of code and conduct the next line (not indented)

# syntax  -   if _______:
#             --->  block of code for 'true'
#             else:
#             --->  block of code for 'false' or nothing

# steps
#   1. define/initialise the variables
#   2. establish your true condition
#   3. decide if action on false is required and include. If no condition then false will skip

#  example
#   discount = 0                      (initialise the variables)
#   amount = int(input("Enter the amount: ")) (initialise the variables)
#
#   if amount>100:                    (establish the true condition)
#   --->  discount = amount*0.20      (block of code to execute upon true condition)
#   elif amount>50:                   (use elif if there are other conditions that need to occur)
#   --->  discount = amount*0.10      (elif code block)
#   else:                             (establish a false condition, if required)
#   --->  discount = amount*0.05      (block of code to execute upon false condition)
#



print("Welcome to the sale, spend under $100 and receive 5% off, spend over $100 and receive 20% off!")
discount = 0
amount = int(input("How much are you spending? "))
if amount > 100:
    discount = amount * 0.20
elif amount > 50:
    discount = amount * 0.10
else:                                  #not required if no condition for false
    discount = amount * 0.05           #not required if no condition for false

print("You have saved: ", discount)
print("Your total is: ", amount-discount)
