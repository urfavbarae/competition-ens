print("X*Y\tI", end="\t")
for i in range(0,11):
    print(i,"\t",end="")
print("")
print("-"*100) 
for i in range(0,11):
    print(i,"\tI",end="")
    print("\t",end="")  
    for j in range(0,11):
        print(i*j,end="")
        if i*j<10:
            print("\t",end="")
        else:
            print("\t",end="")
    print("")
print("-"*100) 