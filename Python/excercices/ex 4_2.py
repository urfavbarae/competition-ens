a=int(input("saisir un nombre : "))
so=0
ec="la somme accumulative est : "
for i in range(1,a+1):
    so=so+i
    if i==1:
        ec=ec+"1"
    else:
        ec=ec+" + "+str(i)    
print(f"{ec} = {so}")
if a==0:
    print("le factoriel est :0! = 1")
else:
    mu=1
    ec2="le factoriel est : "
    for i in range(1,a+1):
        mu=mu*i
        if i==1:
            ec2=ec2+"1"
        else:
            ec2=ec2+" x "+str(i)
    print(f"{ec2} = {mu}")




