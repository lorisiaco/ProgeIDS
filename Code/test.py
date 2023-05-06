#test unit for the code
import unittest
import sys
sys.path.append('..')
from Code import main
from Code import Offerta
from Code import JobData
from Code import init
from Code import User
from Code import UserDB


#test for view_offers method in User class
def test_view_offers(self):
    self.assertEqual(self.view_offers(),JobData.get_offers())

#test for view_offers_r1 method in User class
def test_view_offers_r1(self):
    self.assertEqual(self.view_offers_r1(),JobData.get_offers_sedelegale())

#test for view_offers_r2 method in User class
def test_view_offers_r2(self):
    self.assertEqual(self.view_offers_r2(),JobData.get_offers_ruolo())

#test for view_offers_r3 method in User class
def test_view_offers_r3(self):
    self.assertEqual(self.view_offers_r3(),JobData.get_offers_salarioMAX())

#test for view_offers_r4 method in User class
def test_view_offers_r4(self):
    self.assertEqual(self.view_offers_r4(),JobData.get_offers_salarioMIN())

#test for get_offers method in JobData class
def test_get_offers(self):
    self.assertEqual(self.get_offers(),JobData.get_offers())

#test for get_offers_sedelegale method in JobData class
def test_get_offers_sedelegale(self):
    self.assertEqual(self.get_offers_sedelegale(),JobData.get_offers_sedelegale())

#test for get_offers_ruolo method in JobData class
def test_get_offers_ruolo(self):
    self.assertEqual(self.get_offers_ruolo(),JobData.get_offers_ruolo())

#test for get_offers_salarioMAX method in JobData class
def test_get_offers_salarioMAX(self):
    self.assertEqual(self.get_offers_salarioMAX(),JobData.get_offers_salarioMAX())
    