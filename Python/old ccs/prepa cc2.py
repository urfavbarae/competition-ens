#n=int(input("saisir n: "))
#triangle 1
"""
for i in range(1,n+1):
    print("*"*i)"""
#triangle 2
"""
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)"""
#triangle 3
"""
for i in range(n,0,-1):
    print("*"*i)"""
#triangle 4
"""
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)"""
#la letre z
""" print("*"*n)
for i in range(1,n-1):
    print(" "*((n-1)-i)+"*")
print("*"*n) """
#tri selective
""" l=[5,5,6,4,7,8,5,6,2,1]
le=len(l)
for i in range(le):
    min_inde=i
    for j in range(i+1,le):
        if l[j]<l[min_inde]:
            min_inde=j
    l[i],l[min_inde]=l[min_inde],l[i]
print(l) """
st=""
print(st.isnumeric())
print(st.isalpha())