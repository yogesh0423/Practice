# append()
num = [10, 20, 30, 40,50]
num.append([66, 80])
print(num)
print(num[-1][-1])

# extend()
numbers = [10, 20]

numbers.extend([30, 40])
numbers.extend((50,60))
numbers.extend({70,80})
print(numbers)

#list.insert(index, value)
num1 = [10, 20, 30]
num1.insert(2,40)
print(num1)


#remove() : removes the first occurence of the element
feature_names = [
    "age",
    "salary",
    "Education",
    "Skills"
]
print(feature_names)
feature_names.remove("skills")
print(feature_names)


#pop() : The last element is removed.
print(feature_names)
removed = feature_names.pop()
print(feature_names.pop(2))
print("Removed: ",removed)

# del 
numbers3 = [10, 20, 30, 40, 50]
del numbers3[1:4]
print(numbers3)

# count()
predictions = [1,0,1,1,0,0,1]
print(predictions.count(0))
print(predictions.count(1))

# sort() : changes the original list
numb = [45,56,67,54,32]
numb.sort()
print(numb)

# enumerate() : it provides cleaner way to access both index nad value.
students = [
    "John",
    "Alex"
    "Doe"
]
for index, student in enumerate(students):
  print(index, student)
