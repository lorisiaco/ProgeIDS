# la classe Offerta rappresenta un'offerta di lavoro
class Offerta:
    def __init__(self, id, ruolo, azienda, sedelegale, salario, descrizione):
        # il costruttore accetta cinque argomenti:il codice univoco ID dell'offerta,  il ruolo dell'offerta di lavoro, il codice dell'azienda che offre lavoro , la località e il salario
        # questi valori vengono assegnati alle proprietà dell'oggetto Offerta
        self.id=id
        self.ruolo = ruolo
        self.azienda = azienda
        self.sedelegale = sedelegale
        self.salario = salario
        self.descrizione=descrizione
        