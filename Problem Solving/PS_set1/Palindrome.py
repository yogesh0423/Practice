
def ispalindrome(str, length):
    left = 0
    right = length -1 
    while left <= right:
        if str[left] != str[right]:
            return 0
        left += 1
        right -= 1
    return 1

str = input()
length = int(input())
print(ispalindrome(str, length))
