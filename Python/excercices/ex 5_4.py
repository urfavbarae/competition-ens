"""def somme(a,b):
    return fun(a,b)+a+b
def fun(x,y):
    return 1+somme(x,y)
print(fun(int(input()),int(input())))"""
def ispremier(a):
    for i in range(1,a):
        if a%i==0:
            return False
    return True
