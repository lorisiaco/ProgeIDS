import Offerta
from JobDatabase import JobData

class Azienda:
    def __init__(self,email,cf,nome,sedelegale,passw):
            # il costruttore accetta tre argomenti:il codice univoco ID dell'azienda
            #il nome e il luogo
            self.email=email
            self.cf=cf
            self.nome=nome
            self.sedelegale=sedelegale
            self.passw=passw
            
            

    def add_offer(self, id, title, location, salary):
        # crea un'istanza della classe Offerta con i dettagli dell'offerta di lavoro
        offer = Offerta(id, title, self.idc, location, salary)
        # utilizza il metodo add_of della classe JobOfferDatabase per aggiungere l'offerta di lavoro al database
        JobData.add_of(offer)
    
    def delete_offer(self, x):
        JobData.delete(x)
            
