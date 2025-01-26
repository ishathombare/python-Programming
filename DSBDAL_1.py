# 1.convert into numpy array
import numpy as np 
a=[100,200,300,150,250,400,350]
A=np.array(a)
print(type(A))

#2. Add and multiply
import numpy as np 
a=np.array([10,20,30])
b=np.array([1,2,3])
sum = np.add(a,b) #addition
print(sum)
mul = np.multiply(a,b) #multiplication
print(mul)

#3. combine two array
import numpy as np
sale_jan = np.array([300,400])
sale_feb = np.array([500,600]) 
sales = np. concatenate ((sale_jan,sale_feb))
print(sales)

#4.convert into 1d array
import numpy as np
score= np.array([[80,90],[85,95]])
oneD_array = score.flatten()
print(oneD_array)

#5.reshape into matrix
data = np.array([1,2,3,4,5,6])
matrix_data = data.reshape(2,3)
print(matrix_data)