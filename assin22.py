'''
A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
'''
def digital_root( n):
    sum = 0
    while(n > 0 or sum > 9):
        if(n == 0):
            n = sum
            sum = 0
        sum = sum + int(n % 10)
        n =int(n/ 10)
    return sum