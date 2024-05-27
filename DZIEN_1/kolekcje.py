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

#krotka
miasta = ("Kraków","Lublin","Katowice","Kraków","Gdańsk","Poznań","Kraków")
print(miasta)
print(type(miasta))

print(miasta.count("Kraków"))
print(miasta.index("Lublin"))

#napisz krotkę z imionami, wstaw 4 imiona w tym niektóre nich niech się powtarzają od 2-5 razy
#utwórz listę z indeksami imienia ktore się powtarza

imiona = ("Anna", "Jan", "Kasia", "Anna", "Marek", "Jan", "Anna", "Jan", "Kasia", "Anna")

# Tworzymy listę indeksów, gdzie znajduje się imię "Anna"
#list comprehension
indeksy_anna = [index for index, value in enumerate(imiona) if value == "Anna"]
indeksy_jan = [index for index, value in enumerate(imiona) if value == "Jan"]

print(f"indeksy dla Anna: {indeksy_anna}")
print(f"indeksy dla Jan: {indeksy_jan}")

#zbiór

kolory = {"zielony","czerwony","niebieski","czarny","biały","brązowy","czerwony"}
print(kolory)
print(kolory)
print(kolory)
kolory.add("pomarańczowy")
print(kolory)
kolory.update(["fioletowy","cyjan","żółty"])
print(kolory)
kol_lista = list(kolory)
print(kol_lista)

#słownik
osoba = {
    "imię":"Jan",
    "nazwisko":"Kot",
    "miasto":"Toruń",
    "wiek":54,
    "kupony":[4,2,56,266,123],
    333:764656475
}
print(osoba)
print(osoba["miasto"])
print(osoba["kupony"])
print(osoba["kupony"][2])
print(osoba[333])

print(osoba.keys())
print(osoba.values())
print(osoba.items())

osoba["miasto"] = "Gdańsk"
print(osoba)

osoba["nr_legitymacji"] = "ADF563452"
print(osoba)

#zbuduj słownik z polami: marka,model,pojemnosc_silnika,rocznik i wstaw dowolne dane
#wyśwoetl słownik, wyświel tylko opole marka, dodaj nowe pole cena i przypisz wartość, wyświetl słownik po zmianach


# Tworzymy słownik z danymi o samochodzie
samochod = {
    "marka": "Toyota",
    "model": "Corolla",
    "pojemnosc_silnika": 1.8,
    "rocznik": 2020
}

# Wyświetlamy cały słownik
print("Słownik samochodu:", samochod)

# Wyświetlamy tylko pole "marka"
print("Marka samochodu:", samochod["marka"])

# Dodajemy nowe pole "cena" i przypisujemy wartość
samochod["cena"] = 75000

# Wyświetlamy słownik po zmianach
print("Słownik samochodu po dodaniu pola 'cena':", samochod)
