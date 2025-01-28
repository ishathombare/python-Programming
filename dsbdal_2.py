import numpy as np 
scores = np.array([
    [85, 90, 78, 92, 88],      
    [72, 75, 80, 68, 74],  
    [95, 88, 92, 96, 90],     
    [60, 65, 70, 58, 62],      
    [88, 84, 86, 89, 87]]) 
 #score 3 studend all marks
scores[2] 
# all student marks of 2 subject
scores[:, 1]
# first 3 student & 2 subject marks 
scores[:3, :2]
#last 2 student & last 3 subjects
scores [3:,2:]
# add 5 marks in each marks
scores + 5 
# -10 subject 4 all students
scores [:,3] -10 
# percentage of all students
per= (scores.sum(axis=1)/5)
print(per)
# average score for students
avg = scores.mean(axis=1) 
print(avg)
#total marks scored by each student
total_mark = scores.sum(axis=1)
print(total_mark)
# the highest score in the entire array
h = scores.max()
print(h)
# average score for each subject
e = scores.mean(axis=0)
print(e)
#the lowest average score
low_avg = np.argmin(scores)
print(low_avg+1)