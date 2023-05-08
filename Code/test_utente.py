import unittest
from unittest.mock import patch
from JobDatabase import JobData
from Utente import Utente

class TestUtente(unittest.TestCase):

    @patch.object(JobData, 'get_offers')
    def test_view_offers(self, mock_get_offers):
        # Define test data
        mock_get_offers.return_value = [(1, 'Job title', 'Company name', 'Location', 50000)]

        # Create an instance of the Utente class
        utente = Utente('CF', 'email', 'password', 'Name', 'Age', 'Gender', 'Residence', 'Resume')

        # Call the method being tested
        utente.view_offers()

        # Assert that the output is correct
        expected_output = [(1, 'Job title', 'Company name', 'Location', 50000)]
        self.assertEqual(expected_output, mock_get_offers.return_value)
    
    @patch.object(JobData, 'get_offers_sedelegale')
    def test_view_offers_r1(self, mock_get_offers_sedelegale):
        # Define test data
        mock_get_offers_sedelegale.return_value = [(1, 'Job title', 'Company name', 'Location', 50000)]

        # Create an instance of the Utente class
        utente = Utente('CF', 'email', 'password', 'Name', 'Age', 'Gender', 'Residence', 'Resume')

        # Call the method being tested
        utente.view_offers_r1()

        # Assert that the output is correct
        expected_output = '1 at Job title at Company name in Location for $50,000.00\n'
        self.assertEqual(expected_output, mock_get_offers_sedelegale.return_value)


    @patch.object(JobData, 'get_offers_ruolo')
    def test_view_offers_r2(self, mock_get_offers_ruolo):
        # Define test data
        mock_get_offers_ruolo.return_value = [(1, 'Job title', 'Company name', 'Location', 50000)]

        # Create an instance of the Utente class
        utente = Utente('CF', 'email', 'password', 'Name', 'Age', 'Gender', 'Residence', 'Resume')

        # Call the method being tested
        utente.view_offers_r2()

        # Assert that the output is correct
        expected_output = '1 at Job title at Company name in Location for $50,000.00\n'
        self.assertEqual(expected_output, mock_get_offers_ruolo.return_value)


    @patch.object(JobData, 'get_offers_salarioMAX')
    def test_view_offers_r3(self, mock_get_offers_salarioMAX):
        # Define test data
        mock_get_offers_salarioMAX.return_value = [(1, 'Job title', 'Company name', 'Location', 50000)]

        # Create an instance of the Utente class
        utente = Utente('CF', 'email', 'password', 'Name', 'Age', 'Gender', 'Residence', 'Resume')

        # Call the method being tested
        utente.view_offers_r3()

        # Assert that the output is correct
        expected_output = '1 at Job title at Company name in Location for $50,000.00\n'
        self.assertEqual(expected_output, mock_get_offers_salarioMAX.return_value)


    @patch.object(JobData, 'get_offers_salarioMIN')
    def test_view_offers_r4(self, mock_get_offers_salarioMIN):
        # Define test data
        mock_get_offers_salarioMIN.return_value = [(1, 'Job title', 'Company name', 'Location', 50000)]

        # Create an instance of the Utente class
        utente = Utente('CF', 'email', 'password', 'Name', 'Age', 'Gender', 'Residence', 'Resume')

        # Call the method being tested
        utente.view_offers_r4()

        # Assert that the output is correct
        expected_output = '1 at Job title at Company name in Location for $50,000.00\n'
        self.assertEqual(expected_output, mock_get_offers_salarioMIN.return_value)

if __name__ == '__main__':
    unittest.main()
