dzialanie = input('Wybierz liczbę  z menu: ' '\n'
                  '1 - dodawanie '  '\n'
                  '2 - odejmowanie '  '\n'
                  '3 - mnozenie '  '\n'
                  '4 - dzielenie '  '\n'
                  '5 - potegowanie '  '\n'
                  '6 - dzielenie modulo '  '\n'


)

liczba_1 = float(input("Podaj pierwszą liczbę: "))
liczba_2 = float(input("Podaj drugą liczbę: "))

if dzialanie == 1:
    wynik = liczba_1 + liczba_2
elif dzialanie == 2:
    wynik = liczba_1 - liczba_2
elif dzialanie == 3:
    wynik = liczba_1 * liczba_2
elif dzialanie == 4:
    wynik = liczba_1 / liczba_2
elif dzialanie == 5:
    wynik = liczba_1 ** liczba_2
else:
    wynik = liczba_1 % liczba_2

print(wynik)



