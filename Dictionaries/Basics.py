#Program 1
student = {
    "Name": "Rahul",
    "Age": 21,
    "City": "Nashik"
}
print(student)

#Program 2
student = {
    "Name": "Rahul",
    "Age": 21,
    "City": "Nashik"
}
print("Name :", student["Name"])
print("Age  :", student["Age"])

#Program 3
student = {
    "Name": "Rahul",
    "Age": 21
}
student["City"] = "Mumbai"
print(student)

#Program 4
student = {
    "Name": "Rahul",
    "Age": 21,
    "City": "Nashik",
    "CGPA": 8.9
}
print("Total Key-Value Pairs :", len(student))

#Program 5
student = {
    "Name": "Rahul",
    "Age": 21,
    "City": "Nashik"
}
for key, value in student.items():
    print(key, ":", value)
