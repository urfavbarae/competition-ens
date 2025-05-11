n=int(input("saisir n: "))
c=0
print("les divideur sont : ")
for i in range(1,n):
    if n%i==0:
        print(i,end=" , ")
        c+=i
print()
print(f"la somme des diviseur est : {c}")