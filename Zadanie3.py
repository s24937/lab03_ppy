import getpass
import random

print("PAPIER, KAMIEŃ, NOŻYCE")
liczba_rund = input("wybierz ilość rund gry: ")
runda_wynik = list(range(0, int(liczba_rund)))
if int(liczba_rund) > 0:
    tryb_gry = input("wybierz tryb gry: [wpisz '1'- gra z komputerem, '2'- 2 graczy (hot seats)] ")
    wynik=""
    punkty_gracza=0
    punkty_komputera=0
    punkty_gracza1=0
    punkty_gracza2=0

    if (tryb_gry == '1'):
        print("GRA Z KOMPUTEREM")
        gracz1 = input("nazwij swojego gracza ")

        print("START GRY")
        for i in range(0, int(liczba_rund)):
            print("wybiera: " + gracz1)
            gr1Input = input("wybierz: '1'- kamień, '2'- papier, '3'- nożyce ")

            if int(gr1Input) < 1 or int(gr1Input) > 3:
                print("nieprawidłowa liczba")
                break
            kompInput = random.randint(1, 3)

            if kompInput == 1:
                print("komputer wybrał: kamień")
                if gr1Input == '1':
                    wynik = "REMIS"
                    print(wynik)
                if gr1Input == '2':
                    wynik = "punkt dla gracza"
                    print(wynik + " " + gracz1)
                    punkty_gracza += 1
                if gr1Input == '3':
                    wynik = "punkt dla komputera"
                    print(wynik)
                    punkty_komputera += 1

            if kompInput == 2:
                print("komputer wybrał: papier")
                if gr1Input == '2':
                    wynik = "REMIS"
                    print(wynik)
                if gr1Input == '3':
                    wynik = "punkt dla gracza"
                    print(wynik + " " + gracz1)
                    punkty_gracza += 1
                if gr1Input == '1':
                    wynik = "punkt dla komputera"
                    print(wynik)
                    punkty_komputera += 1

            if kompInput == 3:
                print("komputer wybrał: nożyce")
                if gr1Input == '3':
                    wynik = "REMIS"
                    print(wynik)
                if gr1Input == '1':
                    wynik = "punkt dla gracza"
                    print(wynik + " " + gracz1)
                    punkty_gracza += 1
                if gr1Input == '2':
                    wynik = "punkt dla komputera"
                    print(wynik)
                    punkty_komputera += 1

            runda_wynik[i] = wynik
            print("")



        print("KONIEC GRY")
        print("PODSUMOWANIE WYNIKÓW:")
        for i in range(0, int(liczba_rund)):
            print(runda_wynik[i])
        print("")
        print("punkty gracza: " + str(punkty_gracza))
        print("punkty komputera: " + str(punkty_komputera))

        print("")

        if(punkty_komputera > punkty_gracza):
            print("ZWYCIĘŻA KOMPUTER")
        if (punkty_komputera < punkty_gracza):
            print("ZWYCIĘŻA "+gracz1)
        if(punkty_komputera == punkty_gracza):
            print("REMIS")

    if (tryb_gry == '2'):
        print("2 GRACZY")
        print("nazwij swoich graczy ")
        gracz1 = input("gracz1 ")
        gracz2 = input("gracz2 ")

        print("START GRY")
        for i in range(0, int(liczba_rund)):
            print("wybiera: " + gracz1)
            gr1Input = str(getpass.getpass(prompt="wybierz: '1'- kamień, '2'- papier, '3'- nożyce "))
            if int(gr1Input) < 1 or int(gr1Input) > 3:
                print("nieprawidłowa liczba")
                break


            print("wybiera: " + gracz2)
            gr2Input = str(getpass.getpass(prompt="wybierz: '1'- kamień, '2'- papier, '3'- nożyce "))
            if int(gr2Input) < 1 or int(gr2Input) > 3:
                print("nieprawidłowa liczba")
                break

            print(gracz1, " wybrał ", str(gr1Input))
            print(gracz2, " wybrał ", str(gr2Input))

        # if int(gr1Input) != 1 & int(gr1Input) != 2 & int(gr1Input) != 3:
        #     break
        # if int(gr2Input) != 1 & int(gr2Input) != 2 & int(gr2Input) != 3:
        #     break

            if gr2Input == '1':
                if gr1Input == '1':
                    wynik = "REMIS"
                    print(wynik)
                if gr1Input == '2':
                    wynik = ("punkt dla " + gracz1)
                    print(wynik)
                    punkty_gracza1 += 1
                if gr1Input == '3':
                    wynik = ("punkt dla " + gracz2)
                    print(wynik)
                    punkty_gracza2 += 1

            if gr2Input == '2':
                if gr1Input == '2':
                    wynik = "REMIS"
                    print(wynik)
                if gr1Input == '3':
                    wynik = ("punkt dla " + gracz1)
                    print(wynik)
                    punkty_gracza1 += 1
                if gr1Input == '1':
                    wynik = ("punkt dla " + gracz2)
                    print(wynik)
                    punkty_gracza2 += 1

            if gr2Input == '3':
                if gr1Input == '3':
                    wynik = "REMIS"
                    print(wynik)
                if gr1Input == '1':
                    wynik = ("punkt dla " + gracz1)
                    print(wynik)
                    punkty_gracza1 += 1
                if gr1Input == '2':
                    wynik = ("punkt dla " + gracz2)
                    print(wynik)
                    punkty_gracza2 += 1

            runda_wynik[i] = wynik
            print("")

        print("KONIEC GRY")
        print("PODSUMOWANIE WYNIKÓW:")
        for i in range(0, int(liczba_rund)):
            print(runda_wynik[i])
        print("")
        print("punkty ", gracz1, str(punkty_gracza1))
        print("punkty ", gracz2, str(punkty_gracza2))

        print("")

        if (punkty_gracza2 > punkty_gracza1):
            print("ZWYCIĘŻA " + gracz2)
        if (punkty_gracza2 < punkty_gracza1):
            print("ZWYCIĘŻA " + gracz1)
        if (punkty_gracza2 == punkty_gracza1):
            print("REMIS")









