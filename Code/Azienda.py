import Offerta
from JobDatabase import JobOfferDatabase

class Azienda:
    def __init__(self, idc, nome, luogo ,passw):
            # il costruttore accetta tre argomenti:il codice univoco ID dell'azienda
            #il nome e il luogo
            self.idc=idc
            self.nome=nome
            self.luogo=luogo
            self.passw=passw

    def add_offer(self, id, title, location, salary):
        # crea un'istanza della classe Offerta con i dettagli dell'offerta di lavoro
        offer = Offerta(id, title, self.idc, location, salary)
        # utilizza il metodo add_of della classe JobOfferDatabase per aggiungere l'offerta di lavoro al database
        JobOfferDatabase.add_of(offer)
    
    def delete_offer(self, x):
        JobOfferDatabase.delete(x)
            