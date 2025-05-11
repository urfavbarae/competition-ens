def suit(a):
        if a==1:
            return 1
        elif a==2:
            return 2
        else:
            return suit(a-1) *suit(a-2)
n=int(input("saisir N : "))
for i in range(1,n+1):
    print(f"S{i}={suit(i)}")