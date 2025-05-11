def fact(a):
    if a ==0 :
        return 1
    else :
        fa=1
        for i in range(1,a+1):
            fa*=i
        return fa
def facinv(b):
    j=0
    for i in range(1,b+1):
        j+=1/fact(i)
    return j
print("E=",facinv(int(input("saisir n: "))))
