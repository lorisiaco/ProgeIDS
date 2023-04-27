from JobDatabase import JobData

class Utente:
    def __init__(self,CF,Email,Password,Nome, Etá,Sesso,Residenza ,Resume):
        self.CF=CF
        self.Email=Email
        self.Password=Password
        self.Nome=Nome
        self.Etá=Etá
        self.Sesso=Sesso
        self.Residenza=Residenza
        self.Resume=Resume
    
    def view_offers(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobData.get_offers()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')
    
    def view_offers_r1(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobData.get_offers_sedelegale()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')
    
    def view_offers_r2(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobData.get_offers_ruolo()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')
        
    def view_offers_r3(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobData.get_offers_salarioMAX()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')

    def view_offers_r4(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobData.get_offers_salarioMIN()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')
