risposta = "si"
while risposta == "si":
    a = eval(input("Inserisci il primo numero: "))
    b = eval(input("Inserisci il secondo numero: "))
    risultato = 0
    c = str(input("Inserisci il simbolo dell'operazione(+,-,*,/,**): "))

    if c == "+":
        risultato = a + b
    elif c == "-":
        risultato = a - b
    elif c == "*":
        risultato = a * b
    elif c == "/":
        if b != 0:
            risultato = a / b
        else:
            print("Non puoi dividere per zero.")
    elif c == "**":
        risultato = a ** b

    if b != 0:
        print("Il risultato è:",risultato)

    risposta = input("Vuoi continuare? (si/no): ")

print("Fine programma")
