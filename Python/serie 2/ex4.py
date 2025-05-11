ch=int(input("""choose one shape:
1. carre
2. carre vide
3. triangle 1
4.  triangle 2
5. triangle 3 
6. triangle 4 
7. triangle 5        
"""))
if ch==1:
    n=int(input("entrez le size de carre : "))
    while n<=0:
        n=int(input("entrez le size de carre (n>0) : "))
    for i in range(1,n+1):
        for i in range(1,n+1):
            print("*", end=" ")
        print("")
elif ch==2:
    n2=int(input("entrez le size de vide carre : "))
    while n2<=0:
        n2=int(input("entrez le size de vide carre (n>0) : "))
    for i in range(1,n2+1):
        if i==1 or i==n2:
            for i in range(1,n2+1):
                print("*", end=" ")
            print("")
        else:
            print("*",end=" ")
            for i in range(2,n2):
                print(" ",end=" ")
            print("*")
elif ch==3:
    n3=int(input("entrez le size de triangle 1 : "))
    while n3<=0:
        n3=int(input("entrez le size de triangle 1 (n>0) : "))
    for i in range(1,n3+1):
        c=i
        for i in range(1,c+1):
            print("*",end=" ")
        print("")        
elif ch==4:
    n4=int(input("entrez le size de triangle 2 : "))
    while n4<=0:
        n4=int(input("entrez le size de triangle 2 (n>0) : "))
    for i in range(n4,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print("")
elif ch==5:
    n5=int(input("entrez le size de triangle 3 : "))
    while n5<=0:
        n5=int(input("entrez le size de triangle 3 (n>0) : "))
    for i in range(1,n5+1):
        for j in range(n5-i):
            print(" ",end=" ")
        for f in range(i):
            print("*",end=" ")
        print("")
elif ch==6:
    n6=int(input("entrez le size de triangle 4 : "))
    while n6<=0:
        n6=int(input("entrez le size de triangle 4 (n>0) : "))
    for i in range(n6,0,-1):
        for j in range(i):
            print("*",end=" ")
        print("")
elif ch==7:
    n7=int(input("entrez le size de triangle 5 (il doit etre inpaire): "))
    while n7<=0 or n7%2!=0:
        n7=int(input("entrez le size de triangle 5 (n>0) and (il doit etre inpaire): "))  
    for i in range(1,n7+1):
        n71=n7/2+1.5
        for i in range (1,n71-i):
            print(" ",end=" ")
        for i in range(i+1):
            print("*",end=" ")
        print("")  
            
else: 
    print("choix unvalide")      

        