n = int(input("Enter a number to find its divisors: "))
d = []
for i in range(1, n + 1):
    if n% i == 0:
        d.append(i)
print("The divisors of given number are :",d)
