'''
In ShareChat, there is a sequence of binary integers A1,A2,…,AN. You should answer Q queries on this sequence. In each query, you are given two indices L and R and a binary integer X.

The answer to a query is the smallest index i (L≤i≤R) such that the value Ai⊕X is maximum possible, i.e. equal to max(AL⊕X,AL+1⊕X,…,AR⊕X). Here, ⊕ denotes the bitwise XOR operation.

Input
The first line of the input contains two space-separated integers N and Q.
N lines follow. For each i (1≤i≤N), the i-th of these lines contains a single binary string denoting the number Ai (in binary representation).
The following Q lines describe queries. Each of these lines contains two space-separated integers L and R, followed by a space and a binary string denoting the number X (in binary representation).

Output
For each query, print a single line containing one integer — the answer to that query.

'''

N,Q=map(int,input().split())
N1=[]
L=[]
R=[]
X=[]
t=[0]
for i in range(N):
    t.append(0)
    N1.append(input())
for i in range(Q):
    L1,R1,X1=input().split()
    L.append(int(L1))
    R.append(int(R1))
    X.append(X1)
def st(L,R,N,X,t):
    for j in range(L[i],R[i]+1):
        t[j]=int(N1[j-1],2)^int(X[i],2)
    print(t.index(max(t)))
for i in range(Q):
    st(L,R,N,X,t)