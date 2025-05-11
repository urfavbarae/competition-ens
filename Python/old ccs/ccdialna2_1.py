""" def test(ch):
    l=list(ch)
    i=0
    while i<=len(l):
        if "(" in l:
            index=l.index("(")
            if ")" not in l[index:]:
                return False
            else:
                l.remove(")")
                l.remove("(")
        if "[" in l:
            index=l.index("[")
            if "]" not in l[index:]:
                return False
            else:
                l.remove("]")
                l.remove("[")
        if "{" in l:
            index=l.index("{")
            if "}" not in l[index:]:
                return False
            else:
                l.remove("}")
                l.remove("{")
        i+=1
    if ")" in l or "]" in l or "}" in l:
        return False
    else:
        return True

print(test(input())) """

""" def pr_pi(ch):
    l=list(ch)
    cha=""
    for i in l:
        cha="*"+i+cha
        print(cha,end="*")
        print()
pr_pi(input()) """

""" def tri(l):
    if len(l)<=1:
        return l
    else:
        n=l.pop()
        l1=[]
        l2=[]
        for i in l:
            if i<n:
                l1.append(i)
            else:
                l2.append(i)
        return tri(l1)+[n]+tri(l2)
    
print(tri([5,6,9,6,5,47,4,7,8,5,2,3,2,3,2,3,1,4,1,2])) """