from JobDatabase import JobOfferDatabase

class Utente:
    def __init__(self, CF, password ):
        self.CF=CF
        self.password=password
    
    def view_offers(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobOfferDatabase.get_offers()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')
    
    def view_offers_r1(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobOfferDatabase.get_offers_luogo()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')
    
    def view_offers_r2(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobOfferDatabase.get_offers_ruolo()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')
        
    def view_offers_r3(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobOfferDatabase.get_offers_salarioMAX()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')

    def view_offers_r4(self):
        # utilizza il metodo get_offers della classe JobOfferDatabase per ottenere tutte le offerte di lavoro dal database
        offers = JobOfferDatabase.get_offers_salarioMIN()
        
        # stampa le offerte di lavoro
        for offer in offers:
            id, title, company, location, salary = offer
            print(f'{id} at {title} at {company} in {location} for ${salary:,.2f}')