ch1=input("car1 :")
ch2=input("car2 :")
test=0
i1=0
j1=0
for i in ch1:
    i1+=1
    for j in ch2:
        j1+=1
        if i==j:
            test+=1
if j1/i1==i1 and test==i1:
    print("anagram")
else:
    print("no anagram")
        