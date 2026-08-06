while True:
    mark_math=float(input("Enter marks obtained in Maths: "))
    if (mark_math>100 or mark_math<0):
        print("\nInvalid input enter marks in range 0-100\n")
    else:
        break

while True:
    mark_ai=float(input("Enter marks obtained in Artificial Intelligence: "))
    if (mark_ai>100 or mark_ai<0):
        print("\nInvalid input enter marks in range 0-100\n")
    else:
        break

while True:
    mark_ds=float(input("Enter marks obtained in Data Structure: "))
    if (mark_ds>100 or mark_ds<0):
        print("\nInvalid input enter marks in range 0-100\n")
    else:
        break

while True:
    mark_cloud=float(input("Enter marks obtained in Cloud: "))
    if (mark_cloud>100 or mark_cloud<0):
        print("\nInvalid input enter marks in range 0-100\n")
    else:
        break

while True:
    mark_cyber=float(input("Enter marks obtained in Cybersecurity: "))
    if (mark_cyber>100 or mark_cyber<0):
        print("\nInvalid input enter marks in range 0-100\n")
    else:
        break

tm= mark_math+mark_cyber+mark_cloud+mark_ds+mark_ai
per=(tm/500)*100
print("\n-------------------------------------------------")
print("Marks obtained in Maths :",mark_math)
print("Marks obtained in Artificial Intelligence :",mark_ai)
print("Marks obtained in Data Structure :",mark_ds)
print("Marks obtained in Cloud :",mark_cloud)
print("Marks obtained in Cybersecurity :",mark_cyber)
print("\n")
print("Total marks obatined out of 500 :",tm)
print("Percentage Obatined = ",per)

if per>=40 and per<65:
	print("II Class")
elif per>=65 and per<75:
	print("I Class")
elif per>=75 and per<=100:
	print("Distinction")
elif per<0 or per>100:
	print("Invalid output please retry")
else:
	print("Failed")		
		
	   
   
