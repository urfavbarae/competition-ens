max=5
for i in range(1,11):
    n=float(input(f"saisir le nombre numero {i} : "))
    if i==1 or max<=n:
        max=n
        pos=i
print(f"le nombre maximal {max}, sa position est: {pos}")