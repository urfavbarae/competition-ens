#code nmbr pair 
a,b=int(input("saisir l'intervale : ")), int(input())
while a>=b :
    a,b=int(input("saisir un intervale valide (le premier nombre doit etre inferieur de la dexieme) : ")), int(input())
if a%2!=0:
    print("les nombres impaire dans cette intrvale sont :")
    for i in range(a,b+1,2) :
        print(i,end=" / ")
else: 
    a+=1 # a=a+1
    print("les nombres impaire dans cette intrvale sont :")
    for i in range(a,b+1,2) :
        print(i,end=" / ")
    a-=1
if a%2==0:
    print("""
les nombres paire dans cette intrvale sont :""")
    for i in range(a,b+1,2) :
        print(i,end=" / ")
else: 
    a+=1
    print("""
les nombres paire dans cette intrvale sont :""")
    for i in range(a,b+1,2) :
        print(i,end=" / ")
