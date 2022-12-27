# la classe Offerta rappresenta un'offerta di lavoro
class Offerta:
    def __init__(self, id, title, company, location, salary):
        # il costruttore accetta cinque argomenti:il codice univoco ID dell'offerta,  il titolo dell'offerta di lavoro, il codice dell'azienda che offre lavoro , la località e il salario
        # questi valori vengono assegnati alle proprietà dell'oggetto Offerta
        self.id=id
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary