def voycon(l):
    con=0
    for i in l:    
        l2=[]
        l2=i
        l3=[]
        l4=[]
        for j in l2:
            if j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="A" or j=="E" or j=="I" or j=="O" or j=="U":
                l3.append(j)
            else:
                l4.append(j)
        
        l2=l3+l4    
        st=""
        for f in l2:
            st+=f  
        l[con]=st
        con+=1
    return l  
l2=[] 
nb=int(input("saisir le nombre des element que tu va entrer : "))
for i in range(1,nb+1):
    e=input("saisir l'element : ")
    l2.append(e)
print(voycon(l2))