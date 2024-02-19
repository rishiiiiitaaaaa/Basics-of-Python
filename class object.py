class human :
    x=5
h1=human()
print(h1.x)

class student:
    def __init__(self ,name,age):
        self.name=name
        self.age=age

h2=student("rishita","19")
print(h2.name)
print(h2.age)
h1.x=67
del h1
print(h1.x)