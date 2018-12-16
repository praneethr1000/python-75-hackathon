'''
"What do you know about happiness?" — Yoda

Chef is happy only if three conditions hold:

Chef finished cooking a delicious meal
Chef got AC for a programming problem with an almost correct code
Chef got a new problem with a sequence of integers
Today, all three conditions are satisfied. Chef would like you to feel his happiness and provide him with a solution for this new problem with a sequence of integers. The problem is as follows.

You are given a sequence A1,A2,…,AN. You need to determine if it is possible to choose two indices i and j such that Ai≠Aj, but AAi = AAj. (If it was possible, Chef would be truly happy.)

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing the string "Truly Happy" if it is possible to choose required indices or "Poor Chef" otherwise.



'''

t1=int(input())
for z in range(t1):
    N=int(input())
    t=0
    B=list(map(int,input().split()))
    A=[t]+B
    c=set(A)
    if(len(c)!=len(A)):
        for i in range(1,len(A)):
            for j in range(1,len(A)):
                if((A[i]!=A[j]) and (A[A[i]]==A[A[j]])):
                    t+=1
                    break
            if(t!=0):
                break
        if(t!=0):
            print("Truly Happy")
        else:
            print("Poor Chef")
    else:
        print("Poor Chef")