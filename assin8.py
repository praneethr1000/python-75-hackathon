#There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    x=max(arr)
    y=min(arr)
    z=0
    for i in range(3):
        if arr[i]==x:
            z+=1
    if(z>=2):
        return y   # n: unique integer in the array
    else:
        return x