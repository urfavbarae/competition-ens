# les types des variable
# 1. entier integers(int):  
print(0b1101) #you can convert any number from binaire to decimale by using (0b) in the beginning of the varibale
print(0o3435) #you can convert any number from octal to decimale by using (0o) in the beginning of the varibale
print(0xA2C) #you can convert any number from hexadecimal to decimale by using (0x) in the beginning of the varibale
# 2. reel (float):
print(2.5) # comma defined by . 
print(.4) # you can use just .4 to print 0.4
print(4.) # you can use 4. to print 4.0 
# 4.0 = float 
#4 = int
print(5e3) # 5e3 = 5*10**3 that means e = 10**x #e is always a float
# 3. chaine des caractere strings (str)
print("hello wold") #voir cour 1
# 4. booleenes True False : ## la majuscule is important
print(10>5) #he will write true
print(10<5) #he will write false
# les operateur et les operation 
# + \ - \ * \ / \ ** puissanse \ % la reste de division
print(2**3) #int
print(2**3.) #float
print(6/3) #float ##la divison always float 
print(6/3.) #float
print(6//3) #int ## (//) division entier 
print(9//4) # le resltat est 2 car en enleve la vergule
print(-9//4) # le resltat est -3 car kan9albo ela as8ar entier s8ir mnatija 
# les operation v=avec les chaine du caractere (str)
print("moh"+"amed") #en peut assembler des caractere avec +
print("ter"*5) #we can multiply strings
print(2**2**3) #only on puissansse we beggin from right to left that means we calcul 2**3 than the results X 2**X
# les variable 
## le variable est un milieu de stockage la on stock les valeur 
## nom_variable = valeur (typage dynamique) 
nom = "barae" # la vatriable nom est de type string 
nom = True # la variable nom est de type int
# affectation avec operation
x= 4
x += 3 #equivalent X=X+3
print(x)
x//=7 #equ X= X//7
print(x)
a=6
print(f"{a} + {x} = {a+x}") # you can print like that by using F"{} " and putting the variable here {}
print("{} + {} = {}" .format(a,x,a+x) ) # you can print like that by putting the variable succesivement in the format
print("{1} + {0} = {2}" .format(a,x,a+x) ) # you can manipulate the position by write them from 0 to 2
# la fonction type(); pour afficher le type d'un variable
print(a,type(a))
b=True
print(b,type(b))
# la conversion de type
x="3.14"
y= float(x)
print(y,type(y) ) # only if the string contien ust numbers
x1="455e4"
y1= float(x1)
print(y1,type(y1) ) #we can convert e

