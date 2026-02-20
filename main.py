num_1 = int(input("Please provide a number value: "))
num_2 = int(input("Please provide a number value: "))
num_3 = int(input("Please provide a number value: "))

if num_1 > num_2 > num_3:
  print(num_1, num_2, num_3, sep = ", ")

elif num_1 > num_3 > num_2:
  print(num_1, num_3, num_2, sep = ", ")

elif num_2 > num_1 > num_3:
  print(num_2, num_1, num_3, sep = ", ")

elif num_2 > num_3 > num_1:
  print(num_2, num_3, num_1, sep = ", ")

elif num_3 > num_2 > num_1:
  print(num_3, num_2, num_1, sep = ", ")

elif num_3 > num_1 > num_2:
  print(num_3, num_1, num_2, sep = ", ")

else: 
  print("Invalid")


