import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 3


def metoda_prostokatow(funkcja, poczatek_przedzialu, koniec_przedzialu, krok):
    przyblizenie = 0
    for i in range(int(poczatek_przedzialu / krok), int(koniec_przedzialu / krok)):
        x = i * krok + krok / 2
        y = funkcja(x)
        przyblizenie += y * krok
    return przyblizenie


print('Przyblizenie obliczone metoda prostokatow wynosi', metoda_prostokatow(f, 0, 2, 0.3))


def metoda_prostokatow(funkcja, poczatek_przedzialu, koniec_przedzialu, krok):
    # Utworzenie obiektu wykresu
    fig = plt.figure()

    # Rysowanie przebiegu funkcji oraz asymptot przedzialu dla ktorego obliczamy wartosc calki
    przedzialy = int((koniec_przedzialu - poczatek_przedzialu) / krok)
    x = np.linspace(poczatek_przedzialu - .2, koniec_przedzialu + .2, przedzialy)
    y = funkcja(x)
    plt.axvline(poczatek_przedzialu, color='r', ls='--')
    plt.axvline(koniec_przedzialu, color='r', ls='--')
    plt.grid(True)
    plt.plot(x, y, color='b', linewidth=1)

    # Iteracja po przedzialach (prostokaty)
    przyblizenie = 0
    for i in range(int(poczatek_przedzialu / krok), int(koniec_przedzialu / krok)):
        x = i * krok + krok / 2
        y = funkcja(x)
        przyblizenie += y * krok

        # Wspolrzedne pozwalajace narysowac dany prostokat
        wx = [x - krok / 2, x - krok / 2, x + krok / 2, x + krok / 2, x - krok / 2]
        wy = [0, y, y, 0, 0]
        plt.plot(wx, wy, color='r')

    fig.tight_layout()
    plt.show()

    return przyblizenie


print('Przyblizenie obliczone metoda prostokatow wynosi', metoda_prostokatow(f, 0, 2, 0.3))
