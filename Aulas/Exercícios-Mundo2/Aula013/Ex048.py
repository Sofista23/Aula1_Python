s=0
count=0
for c in range(1,501):
    if c%2!=0 and c%3==0:
        s += c
        count += 1
print("A soma dos {0} valores é {1}.".format(count,s))