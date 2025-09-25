#costOfCoke = 4 * 1.50
#qtyCrisps = 3
#unitCostOfCrisps = 0.80
#costOfBread = 3.50
#qtyMars = 5
#costOfMars = qtyMars * 1.0
#costOfTea = 2 * 2
#costOfCrisps = qtyCrisps *unitCostOfCrisps
#total = costOfMars+costOfCoke+costOfCrisps+costOfTea+costOfBread
#print("the total cost is", total)

#print(".")
#print(".")
#print(".")

#number1 = int(input("Enter first number: "))
#number2 = int(input("Enter second nuber: "))
#sum = number1 + number2
#print("the answer is", sum)

#print(".")
#print(".")
#print(".")

#f = int(input("Enter f temp: "))
#c = (f -32) * 5/9
#print("answer", c)

#print(".")
#print(".")
#print(".")

dd = int(input("day: "))
mm = int(input("month: "))
y = int(input("year: "))
c = int(input("first 2 digits of the year: "))
w=(dd+(13*(mm+1)/5)+y+(y/4)+(c/4)-2*c)%7
print(w)