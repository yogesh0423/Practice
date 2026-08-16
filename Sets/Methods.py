# add()
numbers = {10,20,30}
numbers.add(40)
print(numbers)


# update()
numbers = {10,20,30}
numbers.update({40,50,60})
print(numbers)


# remove()
numbers = {10,20,30,40}
numbers.remove(20)
print(numbers)


# pop()
numbers = {10,20,30,40,50,60,70,120,100,140}
removed = numbers.pop()
print("Removed:", removed)
print("Remaining:", numbers)


# discard()
numbers = {10,20,30,40}
numbers.discard(50)
print(numbers)


# clear()
numbers = {10,20,30,40,50}
numbers.clear()
print(numbers)
