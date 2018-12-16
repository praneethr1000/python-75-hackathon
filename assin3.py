#Print the first n natural numbers, one on each line, in ascending order while making sure no number occurs that contains the character k.
'''
Input
Input consists of two numbers n and k
1 = n = 1000
0 = k = 9
'''
n,k=map(int,input().split())
for x in range(1,n+1):
    if str(k) not in str(x):
        print(x)