#Exercice 1

""" x=int(input("write a number : "))

if x>0:
    print(f"{x} est positive")
    print(f"numbers from 1 to {x} : ",end=" ")
    for i in range(1,x+1):
        if i==x:
            print(i)
        else:
            print(i,end=", ")
elif x==0:  
    print("you entred a 0")
else:
    print(f"{x} est negative") """

#Exercice 2

""" x=[5,2,3,9,2,1,5,6,3,2,1,4,21,2,85,33,12,52,14,25,18,17]

def Even(list):
    l=[]
    for i in list:
        if i%2==0:
            l.append(i)
    return l

def summ(list):
    s=0
    for i in list:
        s+=i
    return s


print(Even(x))
print(summ(x))
print(sum(x)) """

#exercice 4

""" def dics(word):
    d={}
    j=0
    for i in range(0,len(word)):
        if word[i]==" ":
            continue
        else:
            d[j]=word[i].lower()
            j+=1
    
    return d

print(dics("       Hello World  ")) """

#