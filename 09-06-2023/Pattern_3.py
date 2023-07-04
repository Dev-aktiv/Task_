num = int(input("Enter the Number of Rows"))
# k=num+1
for i in range(0, num):
    for j in range(i, num-1):
        print(" * ", end=" ")
    print()

