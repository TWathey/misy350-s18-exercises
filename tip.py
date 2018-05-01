
# get string input
total = int(raw_input("Enter total amount: "))
# get integer input: int() convert string to integer
# float() convert string to floating number
tip = float(raw_input("Enter Tip Rate (such as 0.15): "))
total = total - total * tip
# use string formatting to output result
print "You should pay: $%s" % (total)
