#przykład 1
n = 100
def policz(a,b,c,y=6):
    global n
    n = (a+b)*y-c*n
    return n

print(policz(45,6,78,9))
print(policz(-0.545,-10,5.78,11))
print(policz(2,3,5.66))

print(n)
