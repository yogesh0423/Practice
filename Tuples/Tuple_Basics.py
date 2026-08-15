# Program 1

x = (5,6,7)
y = list(x)
print(y)
print(type(y))
y.append(20)
print(y)
x = tuple(y)
print(x)
print(type(x))


#Program 2

Fruits = ("Mango", "apple", "Grapes", "Banana")
print(Fruits[0])
print(Fruits[-1])


# Program 3

b = (45, 67, 454,23 )
print(len(b))
print(max(b))
print(min(b))

# Program 4

c = ("Python", "Machine Learning", "Data Science")
print(c[0])
print(c[1])
print(c[2])

# Program 5

numbers = (10,20,30,40,50)

print(numbers[0:3])
print(numbers[3:5])
print(numbers[::-1])


# Program 6

numbers = (10,20,30,20,40,20)

print(numbers.count(20))
print(numbers.index(20))


# Program 7

e = ("Age", "Experience", "Salary", "Education")
if "Salary" in e:
  print("Exit")
else:
  print("Not exit")


# Program 8

g = ("Python", "Machine Learning", "Deep Learning", "NLP")
for lang in g:
  print(lang)
