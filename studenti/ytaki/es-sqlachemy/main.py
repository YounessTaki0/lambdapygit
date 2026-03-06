from sqlalchemy.orm import Mapped, mapped_column, Session, DeclarativeBase, relationship
from sqlalchemy import Integer, String, ForeignKey, create_engine
import os

engine = create_engine("postgresql://postgres:admin@localhost:5432/its_database")


class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = "clienti"

    id = mapped_column(Integer, primary_key=True)
    nome = mapped_column(String(100))
    cognome = mapped_column(String(100))

    def __str__(self):
        return f"cliente(nome={self.nome}, cognome={self.cognome})"

    def __repr__(self):
        return f"\ncliente(ID={self.id}, nome={self.nome}, cognome={self.cognome}\n)"


def cls():
    os.system("clear")


cls()


class Ticket(Base):
    __tablename__ = "ticket"

    id = mapped_column(Integer, primary_key=True)
    titolo = mapped_column(String(100))
    stato = mapped_column(String(100))
    data = mapped_column(String(100))

    def __str__(self):
        return f"ticket(titolo={self.titolo}, stato={self.stato}, data={self.data})\n"

    def __repr__(self):
        return f"\tticket(ID={self.id}, titolo={self.titolo}, stato={self.stato}, data={self.data})\n"


class Commento(Base):
    __tablename__ = "commenti"

    id = mapped_column(Integer, primary_key=True)
    titolo = mapped_column(String(100))
    ticket_id = mapped_column(Integer, ForeignKey("ticket.id"))
    descrizione = mapped_column(String(100))
    data = mapped_column(String(100))

    def __str__(self):
        return f"commento(titolo={self.titolo}, ticket_id={self.ticket_id}, descrizione={self.descrizione}, data={self.data})"


Base.metadata.create_all(engine)

while True:

    print(
        "0. Exit\n1. Nuovo Cliente\n2. Nuovo Ticket\n3. Mostra Ticket\n4. Mostra Clienti"
    )
    r = int(input("> "))
    cls()

    if r == 0:
        break

    if r == 1:
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        with Session(engine) as session:
            cliente = Cliente(nome=nome, cognome=cognome)
            session.add(cliente)
            session.commit()
    elif r == 2:
        titolo = input("Titolo: ")
        stato = input("Stato: ")
        data = input("Data: ")
        with Session(engine) as session:
            ticket = Ticket(titolo=titolo, stato=stato, data=data)
            session.add(ticket)
            session.commit()
    elif r == 3:
        print(
            "1. Mostra i ticket aperti\n2. Mostra i ticket chiusi\n3. Cerca un ticket per ID"
        )
        r2 = int(input("> "))
        cls()
        if r2 == 1:
            with Session(engine) as session:
                ticket_aperti = session.query(Ticket).filter_by(stato="Aperto").all()
                print(ticket_aperti)
        elif r2 == 2:
            with Session(engine) as session:
                ticket_chiusi = session.query(Ticket).filter_by(stato="Chiuso").all()
                print(ticket_chiusi)
        elif r2 == 3:
            print("Inserisci l'ID del ticket.")
            id_ticket = int(input("> "))
            ticket = ""
            cls()
            with Session(engine) as session:
                ticket = session.query(Ticket).filter_by(id=id_ticket).one()
                print(ticket)
            print("1. Aggiorna lo stato del ticket\n2. Aggiungi un commento sul ticket")
            r3 = int(input("> "))
            cls()
            if r3 == 1:
                print("Inserisci lo stato. (Aperto/Chiuso)")
                stato = input("> ")
                cls()
                with Session(engine) as session:
                    ticket = session.query(Ticket).filter_by(id=id_ticket).one()
                    ticket.stato = stato
                    session.commit()
                    print("Stato cambiato con successo.")
            if r3 == 2:
                print("Inserisci il titolo del commento.")
                titolo = input("> ")
                cls()
                print("Inserisci la descrizione del commento.")
                desc = input("> ")
                cls()
                print("Inserisci la data del commento.")
                data = input("> ")
                cls()
                with Session(engine) as session:
                    commento = Commento(
                        titolo=titolo, descrizione=desc, data=data, ticket_id=ticket.id
                    )
                    session.add(commento)
                    session.commit()
                    print("Commento aggiunto con successo.")
    elif r == 4:
        with Session(engine) as session:
            print(session.query(Cliente).all())
    print("------------------------------\n")
