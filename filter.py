def prime(x):
    for n in range(2,x):
        if x%n==0:
            return  False
        else:
            return True
filtered=filter(prime,range(10))
print("prime number:",list(filtered))