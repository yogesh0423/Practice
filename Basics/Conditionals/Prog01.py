#Increasing Decreasing program


A, B, C = map(int, input().split())

if C > B and B > A:
    print("Increasing")
elif C < B and B < A:
    print("Decreasing")
else:
    print("Neither")