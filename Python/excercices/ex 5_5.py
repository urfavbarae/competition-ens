def fact(a):
    if a ==0 :
        return 1
    else :
        fa=1
        for i in range(1,a+1):
            fa*=i
        return fa
print(fact(int(input("saisir un nombre : "))))