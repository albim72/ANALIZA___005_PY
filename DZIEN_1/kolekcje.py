print("Kolekcje języka Python!")

a:int=700
print(a)
print(type(a))

a = "siedemset"
print(a)
print(type(a))

#lista
cyfry = [2,6,7,4,8,9,2,4,2,4,5,1,5,8,5,3,2,5,7,8,6,4,6]
print(cyfry)
print(type(cyfry))
print(cyfry[0])
print(cyfry[2])
print(cyfry[2:5])
print(cyfry[-1])

cyfry.append(1)
print(cyfry)
cyfry.insert(3,1)
print(cyfry)
ekstra = [5,5,5,5,5,5,5]

cyfry.extend(ekstra)
print(cyfry)

del cyfry[12]
print(cyfry)
cyfry.remove(7)
print(cyfry)

cyfry.sort()
print(cyfry)

cyfry = cyfry + [6,1,1,1,2,7,9,5]
#konkatenacja list
print(cyfry)

imiona = ["Jan","Anna","Daniel"]
imiona = 4*imiona
print(imiona)

t = "lajkonik"
print(t)
print(t[0])
print(t[4])
print(t[2:6])
print(t[-1])
