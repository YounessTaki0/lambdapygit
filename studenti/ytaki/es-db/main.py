from pathlib import Path
import sqlite3
import os

dbpath = Path(__file__).with_name("netflixdb.sqlite")

con = sqlite3.connect(dbpath)
con.set_trace_callback(print)
cur = con.cursor()
r = ""
c = 0
while (r!="exit"):
    print("1. Visualizza i film.\n2. Visualizza le stagioni.\n3. Visualizza le serie tv.\n")
    r = input("> ")
    os.system("clear")
    if(r == "1"):
        query = '''
            SELECT id, title FROM movie ORDER BY title LIMIT 10
        '''

        cur.execute(query)
        results = cur.fetchall()
        if results:
            for content in results:
                print("ID:",content[0], "| Title:",content[1])
        else:
            print("Nessun documento pubblico trovato.")
        r2 = ""
        while (r2 != "exit"):
            boh = False
            print("1. Pagina Successiva.\n2. Pagina Precedente.\n3. Scegli un id per vedere i dettagli.\n4. Cerca un film")
            r2 = input("> ")
            if(r2 == "1"):
                c += 10
                query = '''
                    SELECT id, title FROM movie ORDER BY title LIMIT 10 OFFSET ?
                '''
            elif(r2 == "2"):
                c -= 10
                query = '''
                    SELECT id, title FROM movie ORDER BY title LIMIT 10 OFFSET ?
                '''
            elif(r2 == "3"):
                boh = True
                id = int(input("> "))
                query = '''
                    SELECT id, title, runtime, release_date FROM movie WHERE id = ?
                '''
                cur.execute(query, (id,))
                results = cur.fetchall()
                if results:
                    for content in results:
                        print("ID:",content[0], "| Title:",content[1], "| Runtime:",content[2], "| Release_date:",content[3])
                else:
                    print("Nessun documento pubblico trovato.")
            elif(r2 == "4"):
                print("Cerca per:\n1. Titolo\n2. Lingua\n3. Anno di uscita")
                r3 = input("> ")
                filtro = ""
                if(r3 == "1"):
                    filtro = input("Inserisci il Titolo: ")

                elif(r3 == "2"):
                    filtro = input("Inserisci la Lingua: ")
                
                elif(r3 == "3"):
                    filtro = input("Inserisci l'Anno di uscita: ")

                query = '''
                    SELECT id, title, runtime, release_date FROM movie WHERE title = ?
                '''
                cur.execute(query, (filtro,))
                results = cur.fetchall()
                if results:
                    for content in results:
                        print("ID:",content[0], "| Title:",content[1], "| Runtime:",content[2], "| Release_date:",content[3])
                else:
                    print("Nessun documento pubblico trovato.")

            else:
                break

            if not boh:
                os.system("clear")
                cur.execute(query, (c,))
                results = cur.fetchall()
                if results:
                    for content in results:
                        print("ID:",content[0], "| Title:",content[1])
                else:
                    print("Nessun documento pubblico trovato.")
        break
    if(r == "2"):
        query = '''
            SELECT id, title FROM season ORDER BY title LIMIT 10
        '''
        cur.execute(query)
        results = cur.fetchall()
        if results:
            for content in results:
                print("ID:",content[0], "| Title:",content[1])
        else:
            print("Nessun documento pubblico trovato.")
        r2 = ""
        while (r2 != "exit"):
            boh = False
            print("1. Pagina Successiva.\n2. Pagina Precedente.\n3. Scegli un id per vedere i dettagli.")
            r2 = input("> ")
            if(r2 == "1"):
                c += 10
                query = '''
                    SELECT id, title FROM season ORDER BY title LIMIT 10 OFFSET ?
                '''
            elif(r2 == "2"):
                c -= 10
                query = '''
                    SELECT id, title FROM season ORDER BY title LIMIT 10 OFFSET ?
                '''
            elif(r2 == "3"):
                boh = True
                id = int(input("> "))
                query = '''
                    SELECT id, title, runtime, season_number FROM season WHERE id = ?
                '''
                cur.execute(query, (id,))
                results = cur.fetchall()
                if results:
                    for content in results:
                        print("ID:",content[0], "| Title:",content[1], "| Runtime:",content[2], "| Season_number:",content[3])
                else:
                    print("Nessun documento pubblico trovato.")
            else:
                break

            if not boh:
                os.system("clear")
                cur.execute(query, (c,))
                results = cur.fetchall()
                if results:
                    for content in results:
                        print("ID:",content[0], "| Title:",content[1])
                else:
                    print("Nessun documento pubblico trovato.")
        break
    elif(r == "3"):
        query = '''
            SELECT id, title FROM tv_show ORDER BY title LIMIT 10
        '''
        cur.execute(query)
        results = cur.fetchall()
        if results:
            for content in results:
                print("ID:",content[0], "| Title:",content[1])
        else:
            print("Nessun documento pubblico trovato.")
        r2 = ""
        while (r2 != "exit"):
            boh = False
            print("1. Pagina Successiva.\n2. Pagina Precedente.\n3. Scegli un id per vedere i dettagli.")
            r2 = input("> ")
            #os.system("clear")
            if(r2 == "1"):
                c += 10
                query = '''
                    SELECT id, title FROM tv_show ORDER BY title LIMIT 10 OFFSET ?
                '''
            elif(r2 == "2"):
                c -= 10
                query = '''
                    SELECT id, title FROM tv_show ORDER BY title LIMIT 10 OFFSET ?
                '''
            elif(r2 == "3"):
                boh = True
                id = int(input("> "))
                query = '''
                    SELECT id, title, created_date, locale FROM tv_show WHERE id = ?
                '''
                cur.execute(query, (id,))
                results = cur.fetchall()
                if results:
                    for content in results:
                        print("ID:",content[0], "| Title:",content[1], "| Created_date:",content[2], "| Locale:",content[3])
                else:
                    print("Nessun documento pubblico trovato.")
            else:
                break

            if not boh:
                os.system("clear")
                cur.execute(query, (c,))
                results = cur.fetchall()
                if results:
                    for content in results:
                        print("ID:",content[0], "| Title:",content[1])
                else:
                    print("Nessun documento pubblico trovato.")
        break