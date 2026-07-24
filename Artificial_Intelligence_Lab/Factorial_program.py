def f(a):
 fact=1
 while(a!=1):
  fact=fact*(a)
  a=a-1
 print(f"Factorial of the given number = ",fact)
 return fact


a=int(input("Enter the number you want to find factorial of: "))
print(f"The number whose factorial is to be found : ",a)

if(a<0):
   print("Factorial does not exist for negative number: ")
elif (a==0 or a==1):
  print("Factorial = 1")  
else:
  b=f(a)


