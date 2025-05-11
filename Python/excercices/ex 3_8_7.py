import datetime
dn=int(input('siasir ta date de naisance : '))
dr=int(input('saisir la date de recrutement : '))
sa=float(input('saisir ton salaire initial : '))
if dn>datetime.date.today().year or dn<datetime.date.today().year-100:
    print('date de naissance unvalid')
elif dr>datetime.date.today().year or dr<datetime.date.today().year-82 or dr<dn+18:
    print('date de recrutement unvalid')
elif sa<0 :
    print('salaire est negative')
else:
    age=datetime.date.today().year-dn
    exp=datetime.date.today().year-dr
    if age<40 and exp>=10:
        print(f'votre salair apres retrais est : {sa-0.2*sa}')
    elif 40<=age<=55 and exp>=15:
        print(f'votre salair apres retrais est : {sa-0.1*sa}')
    elif age>=55 and exp>=25:
        print(f'votre salair apres retrais est : {sa}')
    else:
        print("tu n'a pas de ta9a3od")
    
#datetime.date.today().year= the current year