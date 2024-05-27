#przykład 1

def nk(k):
    return k**0.5+k

n = 100
def policz(a,b,c,y=6):
    global n
    n = (a+b)*y-c*n*nk(b)
    return n

print(policz(45,6,78,9))
print(policz(-0.545,-10,5.78,11))
print(policz(2,3,5.66))

print(n)

#przykład 2

def rank(*lang,nrrank,**inne):
    print(f"ranking języków programowania nr {nrrank} -> 1. {lang[0]}, 2. {lang[1]}. 3. {lang[2]}")

rank("Python","Java","C#","JavaScript",nrrank=56)
rank("Python","C++","Java","C#","JavaScript","TypeScript",nrrank=56)


#przykład 3 -> funkcje anonimowe

print((lambda d:d+112)(3))
s = lambda x,y,z=1:(x-2*z)/(y-x)
print(s(3,5,2))
print(s(6,7))


def multi(n):
    return lambda a:a*n

print(multi(30)(3))

num = [56,7,8,-32,45,24,-564,3,76,1109,-234,45,-435]

parzyste = list(filter(lambda x:x%2==0,num))
print(parzyste)

cube = list(map(lambda x:x**3,num))
print(cube)

#zbuduj liste która bedzie składała się z wartości całkowitch z przedziały [1,100000]
#Każda z wartości ma być kwadratem  wartości

kwadraty = [i**2 for i in range(1, 100_000)]
print(kwadraty[-4:-1])

#napisz funkcję budującą listę o dwolnej długości gdzie elementami listy są dowolne potęgi każxej wartości z zadanego przedzialu
# uzyj tej fukcji w dwoch rożny przypadkach

def generuj_liste(potega,min,max):
    return [i**potega for i in range(min,max)]

p1 = generuj_liste(5,100,112)
p2 = generuj_liste(4,2,16)

print(p1)
print(p2)

#funkcja wyższego rzędu
def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def konkurs(imie,miejsce,punkty):
    return f'uczestnik konkursu: {imie},miejsce: {miejsce}, punkty: {punkty}'

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Anna",12,67))
