int_walls = int(input())
ext_walls = int(input())

total = 0
int_cost = 18
ext_cost = 12

for i in range(int_walls):
    area = float(input())
    total = total + (area * int_cost)

for i in range(ext_walls):
    area = float(input())
    total = total + (area * ext_cost)
print("Total estimated cost:", total, "INR")