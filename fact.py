def fact(n):
    f1=1
    for i in range(1, n+1):
        f1 = f1*i
    return f1

a = int(input("enter number"))
print(fact(a))
        
