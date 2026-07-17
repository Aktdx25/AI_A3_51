def add(a,b):
	return (a+b)
	  
def sub(a,b):
	return a-b
	
def multiply(a,b):
	return a*b

def div(a,b):
	return a/b
	  	  	  	  
print("Select the arithmatic operation you want to perform:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
ch=int(input("Enter Choice 1-4:  "))
if ch==1:
	  num1=float(input("Enter the first number:  "))
	  num2=float(input("Enter the second number:  "))
	  result=add(num1,num2)
	  print(f"Sum= {result}")
elif ch==2:
          num1=float(input("Enter the first number:  "))
          num2=float(input("Enter the second number:  "))
          result=sub(num1,num2)
          print(f"Diffrence= {result}")
elif ch==3:
          num1=float(input("Enter the first number:  "))
          num2=float(input("Enter the second number:  "))
          result=multiply(num1,num2)
          print(f"Result= {result}")	  
elif ch==4:
	  num1=float(input("Enter the first number:  "))
	  num2=float(input("Enter the second number:  "))
	  result=div(num1,num2)
	  print(f"Result= {result}")
else:
  print("Program closed")	  	  
	  
