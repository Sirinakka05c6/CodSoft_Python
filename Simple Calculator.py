print("Simple Calculator")
num1=int(input("\nEnter number1: "))
num2=int(input("Enter number2: "))
choice = input("Enter an operand: ")
print("Result of the calculation performed: ")
if choice=='+':
  print(num1+num2)
elif choice=='-':
  print(num1-num2)
elif choice=='*':
  print(num1*num2)
elif choice=='/':
  print(num1/num2)
elif choice=='%':
  print(num1%num2)
else:
  print("Enter a valid operation choice")
