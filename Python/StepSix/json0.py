import json

d = {"a": 1}
d2 = {2: 1}
l = [1, 2.2]
t = (3, 4)
s = "I am string!"

print(json.dumps(d))
print(json.dumps(d2))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))
