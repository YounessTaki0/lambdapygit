x = ""
y = ""
operazione = ""

fine = 0 #numero finale

utente = True

continuare = ""

programma = ""

while utente == True:
    programma = input("Per calcolatrice standard inserisci 1\nPer calcolatrice di mesi inserisci 2\n")
    if programma.isnumeric() == True:
        programma = int(programma)
        if programma == 1:
            x = input("Inserisci il primo numero: ") #input primo numero
            if x.isnumeric() == True:
                x = int(x)
            else:
                print("Errore valore non numerico")
                continue
            y = input("Secondo numero: ") #input secondo numero
            if y.isnumeric() == True:
                y = int(y)
            else:
                print("Errore valore non numerico")
                continue
            operazione = input("L'operatore: ") #operatore
            if operazione == "+":
                fine = x + y
            elif operazione == "x" or operazione == "*":
                fine = x * y
            elif operazione == "X":
                fine = x * y
            elif operazione == "-":
                fine = x - y
            elif operazione == "/":
                if y == 0:
                    print("Non si divide per 0!")
                else:
                    fine = x / y
            else:
                print("Errore")
            print(fine)
        elif programma == 2: #7mesi 31giorni 4mesi 30giorni
            print("programma 2")
        else:
            print("Errore\nQuale programma vuoi usare?")
            continue


    continuare = input("Per continuare scrivi si\n")

    if continuare != "si":
        break

print("Sei uscito!")