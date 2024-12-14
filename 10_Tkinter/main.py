import tkinter as tk
from random import randint
from PIL import Image, ImageTk

class Gra():
    def __init__(self):
        self.stan = [0, 0, 0]
        self.runda = 0
        self.portfel = 0
        self.wygrana = 0
        self.wygrana_suma = 0

    def losuj(self):
        if self.portfel < 100:
            return -1

        self.wygrana = 0
        self.portfel -= 100
        self.stan = [randint(0, 2), randint(0, 2), randint(0, 2)]
        self.runda += 1
        if len(set(self.stan)) == 1:
            if self.stan[0] == 0:
                self.wygrana = 100
            elif self.stan[0] == 1:
                self.wygrana = 1000
            elif self.stan[0] == 2:
                self.wygrana = 9999

            self.portfel += self.wygrana
            self.wygrana_suma += self.wygrana

gra = Gra()

def aktualizuj_konto():
    gra.portfel += int(kwota_doladowania_entry.get() if kwota_doladowania_entry.get() else 0)
    portfel_label.configure(text='Portfel: ' + str(gra.portfel))
    kwota_doladowania_entry.delete(0, tk.END)

def aktualizuj_gre():
    if gra.losuj() == -1:
        historia_gier.insert(tk.END, f'Za malo srodkow, doladuj konto o 100 i keep gambling!')
        historia_gier.insert(tk.END, f'Pamietaj ze 99% graczy konczy gre przed swoja wielka wygrana!!!')
        historia_gier.see(tk.END) 
        return -1

    portfel_label.configure(text='Portfel: ' + str(gra.portfel))
    for i in range(len(symbole)):
        symbole[i].configure(image=owoce_tk[gra.stan[i]])
    historia_gier.insert(tk.END, 
        f'Runda: {gra.runda}, wygrana: {gra.wygrana}, wygrana w sumie: {gra.wygrana_suma}')
    historia_gier.see(tk.END) 

#Konfiguracja glowego kontenera:
root = tk.Tk()
root.title('Keep Gambling')
root.configure(background='black')
root.geometry('1080x720')


root.grid_columnconfigure(0, weight=1, minsize=200)
root.grid_columnconfigure(1, weight=1, minsize=200)
root.grid_columnconfigure(2, weight=1, minsize=200)
root.grid_columnconfigure(3, weight=1, minsize=200)


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)


portfel_label = tk.Label(root, text='Portfel: 0')
portfel_label.grid(row=0, column=0, columnspan=4, ipady=50, sticky=tk.NSEW)

doladuj_label = tk.Label(root, text='Podaj kwote:')
doladuj_label.grid(row=1, column=0, ipady=100, sticky=tk.NSEW)

kwota_doladowania_entry = tk.Entry(root, text='kwota')
kwota_doladowania_entry.grid(row=1, column=1, columnspan=2, ipadx=50, sticky=tk.NSEW)

guzik = tk.Button(root, text='doladuj', command=aktualizuj_konto)
guzik.grid(row=1, column=3, sticky=tk.NSEW)

wajcha = tk.Button(root, text='wajcha', command=aktualizuj_gre)
wajcha.grid(row=2, column=0, ipadx=25, ipady=100, sticky=tk.NSEW)


# Wczytanie zdjec owocow:
owocki_img = Image.open('owocki.jpg')
img_width, img_height = owocki_img.size
pole_width = img_width // 3
pole_height = img_height // 3

# crop -> funkcja biblioteki PIL, wycina prostokatna czesc z obrazu:
owoce = [
    owocki_img.crop((pole_width, 15, 
            2 * pole_width, pole_height + 15)),
    owocki_img.crop((2 * pole_width - 15, 15, 
            3 * pole_width - 15, pole_height + 15)),
    owocki_img.crop((pole_width, 2 * pole_height - 15, 
            2 * pole_width, 3 * pole_height - 15))
]

# konwersja do odpowiedniego formatu:
owoce_tk = [ImageTk.PhotoImage(image) for image in owoce]


symbol_1 = tk.Label(root, image=owoce_tk[0])
symbol_1.grid(row=2, column=1, ipadx=25, sticky=tk.NSEW)

symbol_2 = tk.Label(root, image=owoce_tk[1])
symbol_2.grid(row=2, column=2, ipadx=25, sticky=tk.NSEW)

symbol_3 = tk.Label(root, image=owoce_tk[2])
symbol_3.grid(row=2, column=3, ipadx=25, sticky=tk.NSEW)

symbole = (symbol_1, symbol_2, symbol_3)

historia_gier_label = tk.Label(root, text='Historia gier:', anchor=tk.W)
historia_gier_label.grid(row=3, column=0, columnspan=4, ipady=50, sticky=tk.NSEW)
historia_gier = tk.Listbox(root)
historia_gier.grid(row=4, column=0, columnspan=4, sticky=tk.NSEW)


root.mainloop()
