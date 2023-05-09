import unittest
from JobDatabase import JobData
from Azienda import Azienda

class TestAzienda(unittest.TestCase):
    def setUp(self):
        # Creazione di un'istanza della classe Azienda per i test
        self.azienda = Azienda('email', 'cf', 'nome', 'sedelegale', 'passw')
        # Creazione di un'istanza della classe JobData per i test
        self.jobdata = JobData()

    def test_add_offer(self):
        # Creazione di un'offerta di lavoro di test
        offer = self.azienda.add_offer('id', 'title', 'location', 'salary')
        # Verifica che l'offerta di lavoro sia stata aggiunta correttamente al database
        self.assertIn(offer, self.jobdata.offers)

    def test_delete_offer(self):
        # Creazione di un'offerta di lavoro di test
        offer = self.azienda.add_offer('id', 'title', 'location', 'salary')
        # Verifica che l'offerta di lavoro sia presente nel database
        self.assertIn(offer, self.jobdata.offers)
        # Eliminazione dell'offerta di lavoro dal database
        self.azienda.delete_offer('id')
        # Verifica che l'offerta di lavoro non sia più presente nel database
        self.assertNotIn(offer, self.jobdata.offers)

if __name__ == '__main__':
    unittest.main()