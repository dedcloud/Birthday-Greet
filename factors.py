a = int(input("[a]>>"))
b = int(input("[b]>>"))

factors = []

for i in [a,b]:
    for j in range(1,i+1):
        if i%j==0:
            factors.append(j)

lcm = 1
print(set(factors))
