x=lambda a:a+20
print(x(5))

x=lambda a,b :a+b
print(x(5,20))

def pow(n):
    return  lambda a:a*n
doub=pow(2)
print(doub(11))