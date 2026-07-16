n, m = map(int, input().split())

for i in range(n, m + 1):
    if m > 10:
        print(f"{i:03d}", end=" ")
    elif m > 100: 
        print(f"{i:04d}", end=" ")
    else:
        print(f"{i:02d}", end=" ")
