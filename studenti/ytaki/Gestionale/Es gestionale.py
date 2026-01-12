class Dipendente:
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.paga_oraria = paga_oraria

    def stipendio(self, numero_ore):
        return numero_ore * self.paga_oraria

    def __str__(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}, CF: {self.codice_fiscale}, Paga Oraria: {self.paga_oraria}"

    def __gt__(self, dipendente2):
        return self.paga_oraria > dipendente2.paga_oraria


class Manager(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria, numero_sottoposti):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.numero_sottoposti = numero_sottoposti

    def stipendio(self, numero_ore):
        bonus = self.numero_sottoposti * 40
        return (numero_ore * self.paga_oraria) + bonus


class Commerciale(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)

    def stipendio(self, numero_ore):
        p = 8
        stipendio = numero_ore * self.paga_oraria
        return stipendio + (stipendio * (p / 100))


manager = Manager("Giovanni", "Rossi", "abcdefg123", 20, 30)
commerciale = Commerciale("Mario", "Rossi", "abcdefg123", 40)
dipendente1 = Dipendente("Luigi", "Verdi", "abcdefg123", 20)
dipendente2 = Dipendente("Luca", "Pelato", "abcdefg123", 20)
print(dipendente1)
print(f"Stipendio: {dipendente1.stipendio(20)}")
print(dipendente1 > dipendente2)
print(commerciale > manager)
dipendenti = [manager, commerciale, dipendente1, dipendente2]


def totale_stipendi():
    somma = 0
    for dipendente in dipendenti:
        somma += dipendente.stipendio(40)
    return somma


print("Totale stipendi dei dipendenti:", f"{totale_stipendi():.0f}")


commerciale1 = Commerciale("Mario", "Rossi", "abcdefg123", 40)
commerciale2 = Commerciale("Luigi", "Verdi", "abcdefg123", 100)
commerciale3 = Commerciale("Luca", "Pelato", "abcdefg123", 20)

commerciali = [commerciale1, commerciale2, commerciale3]


def miglior_commerciale():
    max = 0
    nome = ""
    for commerciale in commerciali:
        if commerciale.stipendio(40) > max:
            max += commerciale.stipendio(40)
            nome = commerciale.nome
    return nome


print("Miglior commerciale:", miglior_commerciale())
