#1ST print on one line
RollNo=101
Name="Rajesh"
print(f"rollno is:{RollNo} name is:{Name}")

#2ND list
x=['a','x','y','z',['d','e','f'],'p','q','r']
x.append('g')
x[4].insert(2,'n')
print(x)

#3RD dict
student={'rollno':100,'name':'ajay'}
student['fees']=4000
print(student)

#4TH add in set
a={2,3,4,5}
a.add(2)
a.add(8)
print(a)

#5TH tuple
x=(2,3,4,5)
y=list(x)
y.append(7)
x=tuple(y)
print(x)