n = int(input("Entrer un nombre entier : "))
d = 1
while d <= n :
    r = n%d
    if r == 0 :
        print(d)
    d = d+1
print("fin")
