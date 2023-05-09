import unittest
import sqlite3
import Offerta
import Utente
import Azienda
import init
from JobDatabase import JobData


class TestJobDatabase(unittest.TestCase):
    def test_get_offers(self):
        #crea database di test con sqlite3
        conn = sqlite3.connect('test1.db')
        c = conn.cursor()
        #crea tabella di test
        c.execute('''CREATE TABLE OfferteLavoro (ID TEXT PRIMARY KEY ,Titolo TEXT,Azienda TEXT,sedelegale TEXT,Ruolo TEXT,Salario TEXT)''')
        #inserisce dati di test
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("2","Titolo2","Azienda2","Sedelegale2","Ruolo2","Salario2"))
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("3","Titolo3","Azienda3","Sedelegale3","Ruolo3","Salario3"))
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("4","Titolo4","Azienda4","Sedelegale4","Ruolo4","Salario4"))
        conn.commit()
        conn.close()
        #estraggo le offerte dal database di test
        jobdata = JobData('test1.db')
        offers = jobdata.get_offers()
        #verifico che le offerte estratte siano quelle inserite
        self.assertEqual(offers[0][0],"1")
        self.assertEqual(offers[1][0],"2")
        self.assertEqual(offers[2][0],"3")
        #elimino il database di test
        conn = sqlite3.connect('test1.db')
        c = conn.cursor()
        c.execute('''DROP TABLE OfferteLavoro''')
        conn.commit()
        conn.close()

    #test add_of
    def test_add_of(self):
        #testiamo con jobs.db 
        jobdata = JobData('jobs.db')
        #creo offerta di test

        offerta = Offerta.Offerta("801","Titolo1","Azienda1","Sedelegale1","Ruolo1","Salario1")
        #aggiungo offerta di test
        jobdata.add_of(offerta)
        #estraggo offerta di test con metodo get_offers_all
        offers = jobdata.get_offers_all()
        #verifico che l'offerta di test sia stata inserita estraendo l'ultima offerta nel db
        self.assertEqual(offers[-1][0],"801")

    #test delete
    def test_delete(self):
        #testiamo con jobs.db 
        jobdata = JobData('jobs.db')
        #creo offerta di test
        offerta = Offerta.Offerta("803","Titolo1","Azienda1","Sedelegale1","Ruolo1","Salario1")
        #aggiungo offerta di test
        jobdata.add_of(offerta)
        #elimino offerta di test
        jobdata.delete("803")
        #estraggo offerta di test con metodo get_offers_all
        offers = jobdata.get_offers_all()
        #verifico che l'offerta di test sia stata eliminata estraendo l'ultima offerta nel db
        self.assertNotEqual(offers[-1][0],"803")

    #test add_ut 
    def test_add_ut(self):
        #testiamo con jobs.db 
        jobdata = JobData('jobs.db')
        #creo utente di test con classe utente
        utente = Utente.Utente("email903","password1","nome1","cognome1","telefono1","citta1","indirizzo1","cap1")
        jobdata.add_ut(utente)
        #estraggo utente di test con metodo get_users
        utenti = jobdata.get_users()
        #verifico che l'utente di test sia stato inserito estraendo l'ultimo utente nel db
        self.assertEqual(utenti[-1][0],"email903")

    #test add_az
    def test_add_az(self):
        #testiamo con jobs.db 
        jobdata = JobData('jobs.db')
        #creo azienda di test con classe azienda
        azienda = Azienda.Azienda("email905","cf4","nome4","sedelegale4","password4")
        jobdata.add_az(azienda)
        #estraggo azienda di test con metodo get_companies
        aziende = jobdata.get_aziende()
        #verifico che l'azienda di test sia stata inserita estraendo l'ultima azienda nel db
        self.assertEqual(aziende[-1][0],"email905")

    #test per route candidati
    def test_get_candidati(self):
        #testiamo con jobs.db 
        jobdata = JobData('jobs.db')
        #creo utente di test con classe utente
        utente = Utente.Utente("email90","password1","nome1","cognome1","telefono1","citta1","indirizzo1","cap1")
        jobdata.add_ut(utente)
        #creo offerta di test
        offerta = Offerta.Offerta("86","Titolo1","Azienda1","Sedelegale1","Ruolo1","Salario1")
        #aggiungo offerta di test
        jobdata.add_of(offerta)
        #aggiungo candidatura di test
        jobdata.add_candidatura(id_utente="email90",id_offerta="86")
        #estraggo candidatura di test con metodo get_candidati
        candidati = jobdata.get_candidati(id_offerta="86")
        #verifico che la candidatura di test sia stata inserita estraendo l'ultimo candidato nel db
        self.assertEqual(candidati[-1][2],"email90")


if __name__ == '__main__':
    unittest.main()