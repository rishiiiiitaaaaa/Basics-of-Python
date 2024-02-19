def trial(x):
    print(x*3)
list=["hie","hello","bye"]
trial(list)

def map(crazy,list):
    for items in list:
        crazy(items)
map(trial,list)