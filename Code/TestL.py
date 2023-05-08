import unittest
import sqlite3
from JobDatabase import JobData
import Azienda
import Offerta
import Reclamo
import Utente

class TestJobData(unittest.TestCase):

    def setUp(self):
        self.db_name = "jobs.db"
        self.jobdata = JobData(self.db_name)
        self.joboffer = Offerta("off_1", "Programmatore Python", "XYZ", "San Francisco", 120000, "Sviluppatore Python")
        self.user = Utente("12345", "mario.rossi@gmail.com", "password", "Mario Rossi", 30, "M", "Milano", "resume")
        self.company = Azienda("xyz@gmail.com", "12345", "XYZ", "San Francisco", "password")
        self.reclamo = Reclamo("rec_1", "12345", "Mario Rossi", "XYZ", "Descrizione reclamo")
        
    def tearDown(self):
        self.jobdata.conn.close()

    def test_add_of(self):
        # Verifica che l'inserimento di un'offerta di lavoro avvenga correttamente
        self.jobdata.add_of(self.joboffer)
        actual = self.jobdata.get_offers()
        expected = [('off_1', 'Programmatore Python', 'xyz', 'San Francisco', 120000, 'Sviluppatore Python')]
        self.assertEqual(expected, actual)

    def test_add_ut(self):
        # Verifica che l'inserimento di un utente avvenga correttamente
        self.jobdata.add_ut(self.user)
        self.jobdata.cursor.execute("SELECT * FROM Utenti WHERE CF='12345'")
        actual = self.jobdata.cursor.fetchone()
        expected = ('12345', 'mario.rossi@gmail.com', 'password', 'Mario Rossi', 30, 'M', 'Milano', 'resume')
        self.assertEqual(expected, actual)

    def test_add_az(self):
        # Verifica che l'inserimento di un'azienda avvenga correttamente
        self.jobdata.add_az(self.company)
        self.jobdata.cursor.execute("SELECT * FROM Aziende WHERE email='xyz@gmail.com'")
        actual = self.jobdata.cursor.fetchone()
        expected = ('xyz@gmail.com', '12345', 'XYZ', 'San Francisco', 'password')
        self.assertEqual(expected, actual)

    def test_add_re(self):
        # Verifica che l'inserimento di un reclamo avvenga correttamente
        self.jobdata.add_re(self.reclamo)
        self.jobdata.cursor.execute("SELECT * FROM Reclamo WHERE ID='rec_1'")
        actual = self.jobdata.cursor.fetchone()
        expected = ('rec_1', '12345', 'Mario Rossi', 'XYZ', 'Descrizione reclamo')
        self.assertEqual(expected, actual)

    def test_get_offers(self):
        # Verifica che il metodo get_offers restituisca tutte le offerte di lavoro
        actual = len(self.jobdata.get_offers())
        expected = 1
        self.assertEqual(expected, actual)

    def test_get_offers_sedelegale(self):
        # Verifica che il metodo get_offers_sedelegale restituisca solo le offerte con il sedelegale corrispondente
        actual = len(self.jobdata.get_offers_sedelegale("San Francisco"))
        expected = 1
        self.assertEqual(expected, actual)