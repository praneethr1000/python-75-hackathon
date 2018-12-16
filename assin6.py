'''
Chef has a sequence A1,A2,…,AN; each element of this sequence is either 0 or 1. Appy gave him a string S with length Q describing a sequence of queries. There are two types of queries:

'!': right-shift the sequence A, i.e. replace A by another sequence B1,B2,…,BN satisfying Bi+1=Ai for each valid i and B1=AN
'?': find the length of the longest contiguous subsequence of A with length ≤K such that each element of this subsequence is equal to 1
Answer all queries of the second type.

Input
The first line of the input contains three space-separated integers N, Q and K.
The second line contains N space-separated integers A1,A2,…,AN.
The third line contains a string with length Q describing queries. Each character of this string is either '?', denoting a query of the second type, or '!', denoting a query of the first type.
Output
For each query of the second type, print a single line containing one integer — the length of the longest required subsequence.



'''

N,Q,K=map(int,input().split())
N1=list(map(int,input().split()))
Q1=list(input())
cnt1=[]
for y in range(len(Q1)):
    cnt1.append(0)
cnt=[]
def long1(N1,cnt):
    for i in range(N):
        x = N1[i]
        cnt[i] += 1
        for j in range(i + 1, N):
            if N1[j] == x:
                cnt[i] += 1
            else:
                break
    return max(cnt)
for y in range(Q):
    cnt=cnt1
    if Q1[y]=='?':
        z=long1(N1,cnt)
        if z<=K:
            print(z)
        else:
            print(K)
    else:
        N1=N1[-1:] + N1[:-1]







