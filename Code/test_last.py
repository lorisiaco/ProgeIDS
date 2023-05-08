import unittest
import sqlite3
from JobDatabase import JobData


class TestJobDatabase(unittest.TestCase):
    def test_get_offers(self):
        #crea database di test con sqlite3
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        #crea tabella di test
        c.execute('''CREATE TABLE OfferteLavoro (ID TEXT PRIMARY KEY ,Titolo TEXT,Azienda TEXT,sedelegale TEXT,Ruolo TEXT,Salario TEXT)''')
        #inserisce dati di test
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("1","Titolo1","Azienda1","Sedelegale1","Ruolo1","Salario1"))
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("2","Titolo2","Azienda2","Sedelegale2","Ruolo2","Salario2"))
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("3","Titolo3","Azienda3","Sedelegale3","Ruolo3","Salario3"))
        conn.commit()
        conn.close()
        #estraggo le offerte dal database di test
        jobdata = JobData('test.db')
        offers = jobdata.get_offers()
        #verifico che le offerte estratte siano quelle inserite
        self.assertEqual(offers[0][0],"1")
        self.assertEqual(offers[1][0],"2")
        self.assertEqual(offers[2][0],"3")
        #elimino il database di test
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute('''DROP TABLE OfferteLavoro''')
        conn.commit()
        conn.close()

    #test add_of
    def test_add_of(self):
        #crea database di test con sqlite3
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        #crea tabella di test
        c.execute('''CREATE TABLE OfferteLavoro (ID TEXT PRIMARY KEY ,Titolo TEXT,Azienda TEXT,sedelegale TEXT,Ruolo TEXT,Salario TEXT)''')
        #inserisce dati di test
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("1","Titolo1","Azienda1","Sedelegale1","Ruolo1","Salario1"))
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("2","Titolo2","Azienda2","Sedelegale2","Ruolo2","Salario2"))
        c.execute('''INSERT INTO OfferteLavoro (ID,Titolo,Azienda,sedelegale,Ruolo,Salario) VALUES (?,?,?,?,?,?)''',("3","Titolo3","Azienda3","Sedelegale3","Ruolo3","Salario3"))
        conn.commit()
        conn.close()
        #estraggo le offerte dal database di test
        jobdata = JobData('test.db')
        offers = jobdata.get_offers()
        #verifico che le offerte estratte siano quelle inserite
        self.assertEqual(offers[0][0],"1")
        self.assertEqual(offers[1][0],"2")
        self.assertEqual(offers[2][0],"3")
        #elimino il database di test
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute('''DROP TABLE OfferteLavoro''')
        conn.commit()
        conn.close()



if __name__ == '__main__':
    unittest.main()