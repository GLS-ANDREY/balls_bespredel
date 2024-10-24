import pygame

a = {"marka": "BMW", "number": "в123гд", "probeg": 200000}
print(a)
a["probeg"] += 1000
print(a)
a["metka"] = "ДТП"
print(a)
del a["metka"]
print(a)

b = {"marka": "Ford", "number": "а456бм", "probeg": 10000}
c = [a, b]
d = {"marka": "Hyundai", "number": "к456ед", "probeg": 7000000}
c.append(d)
for a in c:
    a["probeg"] += 1000
print(c)
