l= ["girafe","tigre","singe","souris"]
voy="aeouiy"
for i in l:
    cpv=0
    cpc=0
    print(f"{i} sa taille est: {len(i)}")
    for j in i:
        if j.isalpha():
            if j in voy:
                cpv+=1
            else:
                cpc+=1
    print("le nombre des voyelles est:",cpv,"le nbr des consonnes est",cpc)

