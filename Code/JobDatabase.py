import sqlite3

# la classe JobOfferDatabase gestisce il database SQLite che contiene le offerte di lavoro
class JobOfferDatabase:
    def __init__(self, db_name):
        # il costruttore accetta il nome del file del database come argomento
        # crea una connessione al database e ottiene un cursore
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # il cursore esegue la query per creare la tabella nel database se non esiste già
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS OfferteLavoro (ID int, Ruolo text, Azienda int, Luogo text, Salario real, Descrizione text)'''
        )
        self.conn.commit()
    
    def add_of(self, offer):
        # il metodo add_offer accetta un oggetto JobOffer come argomento
        # il cursore esegue la query per inserire una nuova riga nella tabella con i dettagli dell'offerta di lavoro
        self.cursor.execute(
            '''INSERT INTO OfferteLavoro VALUES (? , ?, ?, ?, ?, ?)''',
            (offer.id, offer.ruolo, offer.azienda, offer.luogo, offer.salario, offer.descrizione)
        )
        self.conn.commit()
    
    def get_offers(self):
        # il metodo get_offers esegue una query per selezionare tutte le righe presenti nella tabella
        # utilizza il cursore per ottenere i risultati della query e li restituisce
        self.cursor.execute(
            '''SELECT * FROM OfferteLavoro'''
        )
        return self.cursor.fetchall()
    
    def get_offers_luogo(self):
        # il metodo get_offers_luogo esegue una query per selezionare tutte le righe presenti nella tabella
        #in cui il luogo delle offerte corrisponde al luogo inserito dall'utente per la ricerca
        luogo = input("Inserisci il luogo per la ricerca : ")
        self.cursor.execute(
            '''SELECT * 
               FROM OfferteLavoro
               WHERE Luogo = ?''',(luogo)
        )
        return self.cursor.fetchall()
    
    def get_offers_ruolo(self):
        # il metodo get_offers_ruoloesegue una query per selezionare tutte le righe presenti nella tabella
        #in cui il luogo delle offerte corrisponde al ruolo inserito dall'utente per la ricerca
        ruolo = input("Inserisci il ruolo per la ricerca : ")
        self.cursor.execute(
            '''SELECT * 
               FROM OfferteLavoro
               WHERE Ruolo = ?''',(ruolo)
        )
        return self.cursor.fetchall()

    def get_offers_salarioMAX(self):
        #Query che restituisce le offerte con stipendio uguale o superiore 
        saldo = input("Inserisci il Salario minimo per la ricerca : ")
        self.cursor.execute(
            '''SELECT * 
               FROM OfferteLavoro
               WHERE Salario >= ?''',(saldo)
        )
        return self.cursor.fetchall()

    def get_offers_salarioMIN(self):
        #Query che restituisce le offerte con stipendio minore di quello passato 
        saldo = input("Inserisci il Salario massimo per la ricerca : ")
        self.cursor.execute(
            '''SELECT * 
               FROM OfferteLavoro
               WHERE Salario < ?''',(saldo)
        )
        self.conn.commit()

    def delete(self, id):
        #Query per eliminare una offerta dal database
        self.cursor.execute(
            '''DELETE 
               FROM OfferteLavoro
               WHERE ID= ?''',(id)
        )
        return self.cursor.fetchall()


