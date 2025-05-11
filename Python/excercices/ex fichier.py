f=open(".\\excercices\\notes.txt","r")
l=[]

import os
size=os.path.getsize(".\\excercices\\notes.txt")
while size!=f.tell():
    l.append(float(f.readline()))
print(l)

moy=sum(l)/len(l)
print("Moyenne des notes : {:.2f}".format(moy))
f.close()
f=open(".\\excercices\\notes2.txt","a")
for i in l:
    if i<10:
        f.write(str(i)+" redoublant"+"\n")
    else:
        f.write(str(i)+" admis"+"\n")
f.close()