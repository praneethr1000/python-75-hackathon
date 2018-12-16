'''
Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second) or a string in some languages.

If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, [] for Kotlin or "-1 -1 -1".
'''
def race(v1, v2, g):
    if(v2>v1):
        l=[]
        j=0
        k=0
        i=(g*3600)//(v2-v1)
        if i>=3600:
            j+=i//3600
            i=i-(3600*j)
        if i>=60:
            k+=i//60
            i=i-(60*k)
        l.append(j)
        l.append(k)
        l.append(i)
        return l
    else:
        return None