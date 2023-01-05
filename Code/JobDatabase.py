import sqlite3


# la classe JobOfferDatabase gestisce il database SQLite che contiene le offerte di lavoro
class JobData:
    def __init__(self, db_name):
        # il costruttore accetta il nome del file del database come argomento
        # crea una connessione al database e ottiene un cursore
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # il cursore esegue la query per creare la tabella nel database se non esiste già
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS OfferteLavoro (ID  text PRIMARY KEY , Ruolo text, Azienda int, sedelegale text, Salario real, Descrizione text)'''
        )
        self.conn.commit()
        self.conn.close()
    
    def add_of(self, offer):
        # il metodo add_offer accetta un oggetto JobOffer come argomento
        # il cursore esegue la query per inserire una nuova riga nella tabella con i dettagli dell'offerta di lavoro
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''INSERT INTO OfferteLavoro VALUES ( ?, ?, ?, ?, ?, ?)''',
            (offer.id, offer.ruolo, offer.azienda, offer.sedelegale, offer.salario, offer.descrizione)
        )
        self.conn.commit()
        self.conn.close()

    def add_ut(self, utente):
        # Crea una tabella per gli utenti se non esiste già
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Utenti (CF TEXT PRIMARY KEY ,Email TEXT, Password TEXT,Nome  TEXT,Etá  INTEGER,Sesso TEXT,Residenza TEXT, CV Text)""")
        self.conn.commit()
        self.cursor.execute(
            '''INSERT INTO Utenti (CF,Email, Password, Nome, Etá, Sesso, Residenza, CV) VALUES (?, ?, ?, ?, ? ,?, ?, ?)''',
            (utente.CF, utente.Email, utente.Password,utente.Nome,utente.Etá,utente.Sesso,utente.Residenza,utente.Resume)
        )
        self.conn.commit()
        self.conn.close()
    
    def add_az(self, azienda):
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Aziende (email TEXT PRIMARY KEY ,cf TEXT,nome TEXT,sedelegale TEXT,Password TEXT)""")
        self.conn.commit()
        self.cursor.execute(
            '''INSERT INTO Aziende (email,cf, nome, sedelegale, Password) VALUES (?, ?, ?, ?, ?)''',
            (azienda.email,azienda.cf,azienda.nome,azienda.sedelegale, azienda.passw)
        )
        self.conn.commit()
        self.conn.close()
    
    def get_offers(self):
        # il metodo get_offers esegue una query per selezionare tutte le righe presenti nella tabella
        # utilizza il cursore per ottenere i risultati della query e li restituisce
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''SELECT * FROM OfferteLavoro'''
        )
        return self.cursor.fetchall()
        
    
    def get_offers_sedelegale(self):
        # il metodo get_offers_sedelegale esegue una query per selezionare tutte le righe presenti nella tabella
        #in cui il sedelegale delle offerte corrisponde al sedelegale inserito dall'utente per la ricerca
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        sedelegale = input("Inserisci il sedelegale per la ricerca : ")
        self.cursor.execute(
            '''SELECT * 
               FROM OfferteLavoro
               WHERE sedelegale = ?''',(sedelegale)
        )
        return self.cursor.fetchall()
        
    
    def get_offers_ruolo(self):
        # il metodo get_offers_ruoloesegue una query per selezionare tutte le righe presenti nella tabella
        #in cui il sedelegale delle offerte corrisponde al ruolo inserito dall'utente per la ricerca
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        ruolo = input("Inserisci il ruolo per la ricerca : ")
        self.cursor.execute(
            '''SELECT * 
               FROM OfferteLavoro
               WHERE Ruolo = ?''',(ruolo)
        )
        return self.cursor.fetchall()

    def get_offers_salarioMAX(self):
        #Query che restituisce le offerte con stipendio uguale o superiore 
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        saldo = input("Inserisci il Salario minimo per la ricerca : ")
        self.cursor.execute(
            '''SELECT * 
               FROM OfferteLavoro
               WHERE Salario >= ?''',(saldo)
        )
        return self.cursor.fetchall()

    def get_offers_salarioMIN(self):
        #Query che restituisce le offerte con stipendio minore di quello passato 
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        saldo = input("Inserisci il Salario massimo per la ricerca : ")
        self.cursor.execute(
            '''SELECT * 
               FROM OfferteLavoro
               WHERE Salario < ?''',(saldo)
        )
        return self.cursor.fetchall()

    def delete(self, id):
        #Query per eliminare una offerta dal database
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''DELETE 
               FROM OfferteLavoro
               WHERE ID= ?''',(id)
        )
        return self.cursor.fetchall()


