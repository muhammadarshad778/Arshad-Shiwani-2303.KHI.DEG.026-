import numpy as np
arr=np.random.randint(5,50,24).reshape(6,4)

print(arr)
row_1=arr[0:1]
row_3=arr[2:3]

print("----------")
print("Row 1 :" , row_1)
print("Row 3 :" , row_3)
sum1=row_1+row_3
print("Some of Row 1 & 3", sum1)
row_2=arr[1:2]
row_4=arr[3:4]
print("----------")
print("Row 1 :" , row_2)
print("Row 3 :" , row_4)
sum2=row_2+row_4
print("Some of Row 1 & 3", sum2)
print("----------")


arr[4]=sum1
arr[5]=sum2

print("Result")
print("--------------------")
print(arr)