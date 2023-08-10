rows=5
cloums=4

n=4
for num in range(n):
    if num==n-2:
        print("*")
    else:
        print(num)

for hang in range(rows):
    for lie in range(cloums):
        if lie==cloums-1 and ( hang==0 or hang==rows-1):
            print("$",end="")
        else:
            print('*',end="")
    print()


print("----------------------------------------------------------------")
