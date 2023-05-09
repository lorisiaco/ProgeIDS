import unittest
import sqlite3
from JobDatabase import JobData
import Azienda
import Offerta
import Reclamo
import Utente
import unittest
import os
import sqlite3
import time

class TestJobData(unittest.TestCase):
    def setUp(self):
        # Crea un database temporaneo per i test
        self.db_name = ':memory:'
        self.jobdata = JobData(self.db_name)
        self.job_offer = Offerta.Offerta('123', 'Programmatore', 'Google', 'Mountain View', 100000, 'Descrizione dell-offerta')
        self.user = Utente.Utente('1234567890123456', 'mario.rossi@example.com', 'password', 'Mario', 35, 'M', 'Roma', 'CV di Mario Rossi')
        self.company = Azienda.Azienda('info@example.com', '12345678901', 'Google', 'Mountain View', 'password')
        self.complaint = Reclamo.Reclamo('456', '1234567890123456', 'Mario Rossi',  'Descrizione del reclamo')

    def tearDown(self):
        # Elimina il database temporaneo dopo i test
        os.remove(self.db_name)

    def test_add_of(self):
        self.jobdata.add_of(self.job_offer)
        time.sleep(0.9)  # Delay for 0.9 seconds
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM OfferteLavoro")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], ('123', 'Programmatore', 'Google', 'Mountain View', 100000.0, 'Descrizione dell-offerta'))
        conn.close()

    def test_add_ut(self):
        self.jobdata.add_ut(self.user)
        time.sleep(0.9)  # Delay for 0.9 seconds
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utenti")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], ('1234567890123456', 'mario.rossi@example.com', 'password', 'Mario', 35, 'M', 'Roma', 'CV di Mario Rossi'))
        conn.close()

    def test_add_az(self):
        self.jobdata.add_az(self.company)
        time.sleep(0.9)  # Delay for 0.9 seconds
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Aziende")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], ('info@example.com', '12345678901', 'Google', 'Mountain View', 'password'))
        conn.close()

    def test_add_re(self):
        self.jobdata.add_re(self.complaint)
        time.sleep(0.9)  # Delay for 0.9 seconds
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Reclami")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], ('456', '1234567890123456', 'Mario Rossi',  'Descrizione del reclamo'))
        conn.close()

    def test_get_offers(self):
        self.jobdata.add_of(self.job_offer)
        time.sleep(0.9)  # Delay for 0.9 seconds
        rows = self.jobdata.get_offers()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], ('123', 'Programmatore', 'Google', 'Mountain View', 100000.0, 'Descrizione dell\'offerta'))

if __name__ == '__main__':
    unittest.main()