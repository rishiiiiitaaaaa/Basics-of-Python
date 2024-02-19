d={
    "name" : "rishita",
    "age":19,
    "vehicle":["ertica","i20","alto"]
}
print(d)
print(len(d))
x=d["vehicle"]
y=d.get("age")
print(x)
print(y)
d["age"]=21
d.update({"age":"umar"})
d["color"]="black"
d.pop("age")
print(d)