print("=====MY CALCULATOR=====")

num1 = float(input("enter first number:"))
operator = input("enter operator(+,-,*,/):")
num2 = float(input("enter second number:"))
if operator =="+":
  print("result=",num1 + num2)

elif operator =="-":
  print("result=",num1 - num2)

elif operator =="*":
  print("result=",num1 * num2)

elif opertor =="/":
  if num2 != 0:
    print("cannot divide by zero")

else:
  print("invalid operator")