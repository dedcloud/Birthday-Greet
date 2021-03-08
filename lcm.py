print("-"*31)
print("||    LCM OF TWO NUMBERS     ||")
print("-"*31,"\n")

x=int(input("[x]==>"))
y=int(input("[y]==>"))

if x<y: greater=y
elif x>=y: greater=x

while True:
    
    if (greater%x==0) and (greater%y==0):
        lcm = greater
        break
    else:
        greater += 1

print("="*30)
print("LCM(%d,%d)==>"%(x,y),lcm)
print("="*30)
