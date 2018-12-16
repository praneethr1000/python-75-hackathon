'''
Given an array/list [] of n integers , Arrange them in a way similar to the to-and-fro movement of a Pendulum

The Smallest element of the list of integers , must come in center position of array/list.

The Higher than smallest , goes to the right .
The Next higher number goes to the left of minimum number and So on , in a to-and-fro manner similar to that of a Pendulum.
'''

def pendulum(x):
    y=sorted(x)
    n=len(x)
    c=(n-1)//2
    for i in range(1,len(x)+1):
        if i%2 !=0:
            x[c]=y[i-1]
            c+=i
        else:
            x[c]=y[i-1]
            c-=i
    return x