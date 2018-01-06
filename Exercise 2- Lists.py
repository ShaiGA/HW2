#Creating a 7 numbers list
List=[1,3,4,6,7,9813,23]
print('The original list is',List)

# Reversing the list
List2=List[::-1]
print('The reversed list is',List2)

# Is the 3rd num 7?
print ('The third number in the reversed list is',List2[2])
if List2[2]==7:
    print ('BOOM!')
