from random import randint

class Gra():
    def __init__(self):
        self.stan = [0, 0, 0]
        self.runda = 0
        self.wygrana = 0

    def czy_wygrana(self):
        return ((self.stan[0] in range(0, 6) and
           self.stan[1] in range(0, 6) and
           self.stan[2] in range(0, 6))
           or
           ((self.stan[0] in range(6,9) and
           self.stan[1] in range(6,9) and
           self.stan[2] in range(6,9))
           or
           (self.stan[0] == 9 and
           self.stan[1] == 9 and
           self.stan[2] == 9)))


    def losuj(self):
        self.stan = [randint(0, 9), randint(0, 9), randint(0, 9)]
        self.runda += 1
        nagroda = 0
        if self.czy_wygrana():
            if self.stan[0] in range(0, 6):
                nagroda = 100
            elif self.stan[0] in range(6, 9):
                nagroda = 1000
            elif self.stan[0] == 9:
                nagroda = 9999

            self.wygrana += nagroda
            return nagroda
        else:
            return 0


bandyta = Gra()
for i in range(10):
    bandyta.losuj()
    print(bandyta.stan)
    print(bandyta.runda)
    print(bandyta.wygrana)


