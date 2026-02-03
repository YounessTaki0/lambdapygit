from time import sleep
import os
from pathlib import Path

file = Path("tomogotchi.csv")


class Toma:
    def __init__(self, nome, fame, felicità, stanchezza):
        self.nome = nome
        self.fame = fame
        self.felicità = felicità
        self.stanchezza = stanchezza

    def mangia(self):
        if self.fame - 15 < 0:
            self.fame = 0
        else:
            self.fame -= 15

    def gioca(self):
        self.felicità += 20
        self.stanchezza += 15

    def dormi(self):
        if self.stanchezza - 100 < 0:
            self.stanchezza = 0
        else:
            self.stanchezza -= 100
        self.fame += 50
        if self.felicità - 80 < 0:
            self.felicità = 0
        else:
            self.felicità -= 80

    def __str__(self):
        return f"{self.nome}\t| Fame: {self.fame} | Felicità: {self.felicità} | Stanchezza: {self.stanchezza}"

class Multi_toma:
    def __init__(self, lista_toma):
        self.lista_toma = lista_toma
    
    def scegli_toma(self, nome):
        for toma in self.lista_toma:
            if toma.nome.lower() == nome.lower():
                return toma
        return 1
    
    def aggiungi_toma(self, nome):
        for toma in self.lista_toma:
            if toma.nome.lower() == nome.lower():
                return 1
        toma = Toma(nome, 100, 0, 0)
        self.lista_toma.append(toma)
        return 0
    
    def rimuovi_toma(self, nome):
        for toma in self.lista_toma:
            if toma.nome.lower() == nome.lower():
                self.lista_toma.remove(toma)
                return 0
        return 1
    
    def to_csv(self):
        with open(file, "w") as f:
            for toma in self.lista_toma:
                f.write(f"{toma.nome},{toma.fame},{toma.felicità},{toma.stanchezza}\n")

    def from_csv(self):
        lista_toma = []
        with open(file, "r") as f:
            for line in f:
                nome, fame, felicità, stanchezza = line.strip().split(",")
                toma = Toma(nome, int(fame), int(felicità), int(stanchezza))
                lista_toma.append(toma)
        if len(lista_toma) > 0:
            self.lista_toma = lista_toma

    def __str__(self):
        risultato = ""
        for toma in self.lista_toma:
            risultato += str(toma) + "\n"
        return risultato


lista_toma = [
    Toma("Bob", 100, 0, 0),
    Toma("Pou", 100, 0, 0),
    Toma("Jack", 100, 0, 0),
    Toma("Mike", 100, 0, 0),
    Toma("Daisy", 100, 0, 0),
    Toma("Luigi", 100, 0, 0),
]

to_multi = Multi_toma(lista_toma)
to_multi.from_csv()


os.system("clear")
print("Benvenuto al Tomogotchi Game.")

nome = input(f"Scegli il tuo Tomogotchi tra quelli disponibili:\n{to_multi}\n> ")
while (to_multi.scegli_toma(nome)) == 1:
    os.system("clear")
    print("Errore: Tomogotchi non trovato.")
    nome = input(f"Scegli il tuo Tomogotchi tra quelli disponibili:\n{to_multi}\n> ")
os.system("clear")
toma = to_multi.scegli_toma(nome)
print("Tomogotchi selezionato con successo.")
sleep(1)
os.system("clear")
print(toma)

while True:

    print(
        f"1. Dai da mangiare a {toma.nome}.\n2. Gioca con {toma.nome}.\n3. Fai dormire {toma.nome}.\n4. Aggiungi un nuovo Tomogotchi.\n5. Elimina un Tomogotchi\n6. Scegli un altro Tomogotchi\n7. Termina il programma."
    )
    r = int(input("> "))
    os.system("clear")
    if r == 1:
        toma.mangia()
    elif r == 2:
        toma.gioca()
    elif r == 3:
        toma.dormi()
    elif r == 4:
        nome = input(f"Inserisci il nome del Tomogotchi da aggiungere tra quelli disponibili:\n{to_multi}\n\n> ")
        while (to_multi.aggiungi_toma(nome)) == 1:
            os.system("clear")
            print("Errore: Tomogotchi già esistente.")
            nome = input(f"Inserisci il nome del Tomogotchi da aggiungere tra quelli disponibili:\n{to_multi}\n\n> ")
        os.system("clear")
        to_multi.aggiungi_toma(nome)
        print("Tomogotchi aggiunto con successo.")
    elif r == 5:
        nome = input(f"Inserisci il nome del Tomogotchi da eliminare tra quelli disponibili:\n{to_multi}\n\n> ")
        while (to_multi.rimuovi_toma(nome)) == 1:
            os.system("clear")
            print("Errore: Tomogotchi non trovato.")
            nome = input(f"Inserisci il nome del Tomogotchi da eliminare tra quelli disponibili:\n{to_multi}\n\n> ")
        os.system("clear")
        to_multi.rimuovi_toma(nome)
        print("Tomogotchi eliminato con successo.")
    elif r == 6:
        nome = input(f"Scegli il tuo Tomogotchi tra quelli disponibili:\n{to_multi}\n> ")
        while (to_multi.scegli_toma(nome)) == 1:
            os.system("clear")
            print("Errore: Tomogotchi non trovato.")
            nome = input(f"Scegli il tuo Tomogotchi tra quelli disponibili:\n{to_multi}\n> ")
        os.system("clear")
        print("Tomogotchi selezionato con successo.")
        toma = to_multi.scegli_toma(nome)
    elif r == 7:
        s = "Salvataggio in corso"
        for i in range(4):
            os.system("clear")
            print(s)
            s += "."
            sleep(0.2)
        os.system("clear")
        break
    os.system("clear")
    print(toma)

to_multi.to_csv()