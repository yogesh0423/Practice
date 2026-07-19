# Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)


#Print the multiplication table of a number (entered by user).
num = int(input("Enter a number:"))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#Calculate the sum of all numbers from 1 to 100 using a for loop.
sum = 0
for i in range(1, 101):
    print(i)
    sum += i
print(sum)


#Print a right-angled triangle pattern of stars using a for loop.
for i in range(1, 5):
    print("*" * i)
    
