f=open("trial.txt",'w')
f.write("hiiiififhsjc")
f.close()
f=open("trial.txt",'r')
print(f.read())

f=open("trial.txt",'r')
print(f.read())
print(f.readline(1))
print(f.read(24))
print(f.readline(2))
for x in f:
    print(x)