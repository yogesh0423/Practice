# update
student = {
    "Name": "Yogesh",
    "Age": 20,
}

student.update({"Age": 22,
               "City" : "Nashik",
                "Salary" : [25000, 20000]
                })
print(student)


#pop
student3 = {
    "Name": "Yogesh",
    "Age": 20,
    "City": "Nashik"
}

item = student3.popitem()
print(item)

print(student3)


# Accessing keys, values and items
student4 = {
    "Name": "Yogesh",
    "Age": 20,
    "City": "Nashik"
}

print(student4.keys())
print(student4.values())
print(student4.items())


# Dict to list typecasting
student5 = {
    "Name": "Yogesh",
    "Age": 20,
    "City": "Nashik"
}

print(list(student5.keys()))
print(list(student5.values()))
print(list(student5.items()))


# Nested Dict
student7 ={
    "studnet11": {
        "Name": "Yogesh",
        "Age": 20,
        "CGPA": 7.86
    },
    "student12": {
        "Name": "Rahul",
        "Age": 21,
        "CGPA" : 8.56
    }
}
print(student7)
