userin = 1
array = [] 
while userin != 0 :
     userin = int(input(" Enter the salaries "))
     array.append(userin)
x = len(array)
z = sum(array)
y = z/x
p = 0
print (" The average is ", y)
for loop in range (x):
    print (array[p] , "is", array[p]/z*100 , "% of the whole value " )
    p=p+1
