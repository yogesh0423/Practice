n = int(input())
first = 0
second = 0

while n:
    digit = n % 10
    if digit >= first:
        second = first
        first = digit
    elif digit > second:
        second = digit
    n //= 10

print(first * second)


"""
Example:
Input: n = 31
Output: 3
"""
