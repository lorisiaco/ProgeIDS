# Software Requirement Engineering (Standard IEEE 830)
## 1 - Introduzione
### Scopo ###
Lo scopo della nostra web app è quella di far visualizzare le varie offerte di lavoro agli utenti del sito affinche possano trovare una mansione da loro interessata. Nel caso delle aziende permette di pubblicare offerte di lavoro in determinate zone, con un determinato salario per non avere piu la mancanza di personale che li ha portarti alla pubblicazione dell'annuncio.
### Definizioni ###
*Offerta* : è caratterizzata da varie informazioni, il salario, la descrizione, il luogo di lavoro, la mansione da svolgere.
*Utente* : è colui che ricerca, visualizza le varie offerte di lavoro per cui intende candidarsi.

*Azienda* : é colei che pubblica gli annunci, ossia crea le Offerte di lavoro. Può vedere i vari candidati agli annunci e decidere se accettarli o rifiutarli.

*Reclamo* : redatto da un Utente non soddisfatto, può essere aperto per esempio da una non trasparenza o addiritturà da una falsità dell'Offerta di lavoro dell'Azienda.
## 2 - Descrizione Generale
### Prospettiva del Prodotto ###
La prospettiva del prodotto è quello di semplificare ed ottimizzare la fase di recruting parte Utente e Azienda grazie alla nostra webapp.
### Funzionalità del Prodotto ###
*Funzioni per l'Utente*:
- Registrazione Profilo
- Login Profilo
- Ricerca tramite keyword delle Offerte
- Visualizzazione delle Offerte 
- Possibilità di candidarsi alle Offerte
- Possibilità di effettuare Reclami

*Funzioni per l'Azienda*:
- Registrazione Profilo
- Login Profilo
- Creazione e Publlicazione Offerte
- Visualizzazione candidati Offerte
- Possibilità di accettare o rifiutare le Offerte
### Caratteristiche Utente ###
Dato che la webapp è rivolta ad un target di età che va dai 18-70 anni, l'interfaccia è semplice ed intuitiva proprio per semplificare l'esperienza ed renderla adatta a tutti, quindi non necessita una formazione per l'utilizzo da parte dell'utente finale.
### Vincoli ###
PENSARE

PENSARE 
## 3 - Requisiti Specifici
### Interfaccia Utente ###
Il sistema software deve possedere un'interfaccia semplice, intiutiva e chiara per poter essere utilizzata da più persone possibili.
### Interfaccia HardWare ###
Il sistema software non necessita nessun sistema HardWare
### Requisiti Funzionali ###
*Autenticazione*:
- Registrazione Utente : per la creazione del proprio account l'utente deve inserire vari dati tra cui: i vari data anagrafici(nome,cognome,età) una email, una password e inoltre è richiesto l'annessione del Curriculum Vitae.
-Registrazione Azienda : per la creazione del proprio account l'azienda deve inserire vari dati tra cui: i vari data anagrafici(nome,PIVA) una email, una password.
- Per ogni email deve esistere un unico account, non è permessa la duplicazione.
- Login : l'accesso al propio account è realizzato inserendo l'apposita email e password fornite durante la fase di Registrazione.

*Area Personale Utente* :
- Cerca Offerte per Professione : mostra le Offerte relative alla mansione richiesta data in input.
- Cerca Offerte per Salario : mostra le Offerte relative allo stipendio richiesto dato in input.

*Area Personale Azienda* :
-Carica Offerta : permette di pubblicare un'offerta di lavoro.
-Vedi Candidatura : permette di visualizzare l'elenco dei candidati ai vari annunci.
### Requisiti non Funzionali ###
*Area Personale Utente* :
- Effettua Reclamo : crea un reclamo
### Requisiti sulle Performance ###
Essendo una webapp relativamente leggera e semplice, non c'è bisogno di dispositivi con performance elevate, basta una comune connesione ad internet ed un qualsiasi disposivo per la visualizzazione del sito.





