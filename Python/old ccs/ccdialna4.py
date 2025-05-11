def u(n):
    if n==0:
        return 2
    elif n==1:
        return 3
    return (2/3)*u(n-2)-(1/4)*u(n-1)
n=int(input("saisir N:"))
for i in range (0,n+1):
    print(f"s{i}={u(i)}")