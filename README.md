name=input("enter your name")
place=input("enter your adress")
print("my name is ",name,"My adress is",place)



n=int(input("enter a no"))
empty=[]
for i in range(1,n+1):
      if n%i==0:
         print(i)
      empty.append(i)
      print(empty)


for i in range(100,-1,-2):
      print(i)