'''There is a contest with interactive problems where N people participate.
Each contestant has a known rating. Chef wants to know which contestants will not forget to flush the output in interactive problems.
Fortunately, he knows that contestants with rating at least r never forget to flush their output and contestants with rating smaller than r always forget to do it. Help Chef!


Input
The first line of the input contains two space-separated integers N and r.
Each of the following N lines contains a single integer R denoting the rating of one contestant.


Output
For each contestant, print a single line containing the string "Good boi" if this contestant does not forget to flush the output or "Bad boi" otherwise.

'''

N,r=map(int,input().split())
for i in range(N):
	R=int(input())
	if R>=r:
		print("Good boi")
	else:
		print("Bad boi")