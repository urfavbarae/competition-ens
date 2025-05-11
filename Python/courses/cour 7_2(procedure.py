"""
algorithme
variable 
    procedure Somme (a,b,c:reel)
        variable p:reel
        debut
        p<-a+b+c
        ecrire("la somme est :",p)
    finprocedure
    procedure permutation(x,y:reel)
        variable z:reel
        debut
        z<-x
        x<-y
        y<-z
    finprocedure
"""
def per(a,b):
    c=a
    a=b
    b=c
x,y=int(input()),int(input())
print(x,y)
per(x,y)
print(x,y)
