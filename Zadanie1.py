print("wpisz liczby rozdzielone przecinkami, bez żadnych spacji")

input = input()

for i in range(0, len(input)):
    tab_liczb = input.split(",")

print("wpisane liczby to: ", tab_liczb)
for i in range(0, len(tab_liczb)):
    tab_liczb[i] = int(tab_liczb[i])

maxLiczba = 0
minLiczba = tab_liczb[0]

for i in range(0, len(tab_liczb)):

    if maxLiczba < tab_liczb[i]:
        maxLiczba = tab_liczb[i]
    if minLiczba > tab_liczb[i]:
        minLiczba = tab_liczb[i]

print("Maksymalna liczba wynosi: ", maxLiczba)
print("Minimalna liczba wynosi: ", minLiczba)