num = int(input("Enter the Number of Rows"))
for i in range(0,num):
    print(''*(num-i-1)+'  * '*(i+1))
for j in range(num-1,0,-1):
    print(''*(num-j)+'  * '*(j))
