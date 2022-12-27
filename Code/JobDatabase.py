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
            '''CREATE TABLE IF NOT EXISTS OfferteLavoro (ID int, title text, company int, location text, salary real)'''
        )
        self.conn.commit()
    
    def add_of(self, offer):
        # il metodo add_offer accetta un oggetto JobOffer come argomento
        # il cursore esegue la query per inserire una nuova riga nella tabella con i dettagli dell'offerta di lavoro
        self.cursor.execute(
            '''INSERT INTO job_offers VALUES (? , ?, ?, ?, ?)''',
            (offer.id, offer.title, offer.company, offer.location, offer.salary)
        )
        self.conn.commit()
    
    def get_offers(self):
        # il metodo get_offers esegue una query per selezionare tutte le righe presenti nella tabella
        # utilizza il cursore per ottenere i risultati della query e li restituisce
        self.cursor.execute(
            '''SELECT * FROM OfferteLavoro'''
        )
        return self.cursor.fetchall()


