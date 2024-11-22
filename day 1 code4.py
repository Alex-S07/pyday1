b=[]
a=int(input('enter a number'))
for i in range(1,a+1):
    if a%i==0:
       c=b.append(i)
print(b)