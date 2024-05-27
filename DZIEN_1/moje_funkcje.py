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



