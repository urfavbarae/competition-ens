
def sorting(l):
  j=0
  for i in l:
      st=""
      l[j]=sorted(i,reverse=True)
      for f in l[j]:
        st+=f  
      l[j]=st
      j+=1
  return l  
l2=[]
n=int(input("saisir le nombre des element que tu va entrer : "))
for i in range(1,n+1):
  e=input("saisir l'element : ")
  l2.append(e)
print(sorting(l2))