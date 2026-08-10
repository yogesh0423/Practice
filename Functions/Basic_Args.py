#Program 1
def greet(name = "student"):
  print("Hello", name)

greet()
greet("Yogesh")



#Program 2
def function(name, city):
  print("Name:", name)
  print("City:", city)

function(city = "Mumbai", name = "Yogesh")



#Program 3
def sum_numbers(*args):
  total = 0
  for num in args:
    total += num
  return total

sum_numbers(1,2,3,4,5)



#Program 4
def display(**kwargs):
  print(kwargs)

display(name="Rahul", age=21, city="Nashik")
