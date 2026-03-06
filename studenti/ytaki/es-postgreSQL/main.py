import psycopg2
from psycopg2 import sql

# Dati di connessione (quelli del tuo comando Docker)
config = {
    "host": "127.0.0.1",
    "user": "postgres",
    "password": "admin",  # La tua password Docker
    "port": "5432",
    "database": "postgres",
}

user = input("Inserisci l'username: ")
password = input("Inserisci la password: ")
login = False

with psycopg2.connect(**config) as con:
    with con.cursor() as cur:

        query = """
            SELECT password FROM cliente WHERE username = %s
        """
        cur.execute(query, (user,))
        results = cur.fetchone()

        if not results:
            print("Username errato.")
        elif results[0] == password:
            print("Login successful!")
            login = True
        else:
            print("Password errata.")

        if login:
            query = """
                SELECT id FROM cliente WHERE username = %s
            """
            cur.execute(query, (user,))
            id_cliente = cur.fetchone()

            query = """
                SELECT saldo FROM conto WHERE id = %s
            """
            cur.execute(query, (id_cliente,))
            saldo = cur.fetchone()

            print("Saldo disponibile:", saldo[0])
            importo = input("Importo bonifico: ")

            query = """
                    UPDATE conto
                    SET saldo = saldo - %s
                    WHERE id = %s
                """
            cur.execute(query, (importo, id_cliente))

            query = """
                SELECT saldo FROM conto WHERE id = %s
            """
            cur.execute(query, (id_cliente,))
            saldo = cur.fetchone()

            print("Bonifico effettuato.")
            print("Saldo attuale:", saldo[0])
