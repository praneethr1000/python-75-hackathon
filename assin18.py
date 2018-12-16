'''
Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
'''
def switcheroo(i):
    i=list(i)
    for x in range(len(i)):
        if i[x]=='a':
            i[x]='b'
        elif i[x]=='b':
            i[x]='a'
    str=''.join(i)
    return str