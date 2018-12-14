#Seperator and end in print statements

print(1,2,3,4,sep='*')
#Output: 1*2*3*4

print(1,2,3,sep='*',end='$')
#Output: 1*2*3$

print("\n")  #This is for new line


name="Praneeth"
print('I am {}'.format(name))  #format command where curly braces {} are used as placeholders.
#Output :I am Praneeth

lastname="Reddy"
firstname="Praneeth"
print('I am {1} {0}'.format('lastname','firstname')) #we can specify the order using numbers
#Output: I am Praneeth Reddy

#format strings using % operator

x=200.56789
print("The value of x is %4.3f" %x)
#Output: 200.568
