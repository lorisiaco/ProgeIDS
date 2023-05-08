# ProgeIDS
![alt text](https://github.com/lorisiaco/ProgeIDS/blob/main/Code/maxresdefault.jpg)

Scopo del progetto è quello di creare una webapp che permetta di connettere i singoli individui che cercano lavoro con le aziende che hanno delle posizioni libere da riempire.
## Documentazione
La seguente documentazione comprende i documenti realizzati per la progettazione del problema, verranno prima elencati i diagrammi delle classi in UML poi la documentazione del codice (javadoc).

### ANALISI REQUISITI
Dopo un' attenta analisi dei requisiti abbiamo identificato:
- [REQUISITI](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/SoftwareRequirementEngineering.md)

### UML
Abbiamo realizzato i vari diagrammi grazie a STARUML.
Sono nella cartella [Documetations/UML](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML)
- [CASI D'USO](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/UseCaseDiagram/UseCaseDiagram.png)
- [ATTIVITÀ](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/ActivityDiagram/ActivityDiagram.png)
- [CLASSI](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/ClassDiagram/ClassDiagram.png)
- [STATE MACHINE AZIENDA](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/StateMachineDiagram/StateMachineDiagramAzienda.png)
- [STATE MACHINE UTENTE](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/StateMachineDiagram/StateMachineDiagramUtente.png)
- [SEQUENZE](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/SequenceDiagramDiagram/SequenceDiagram.png)



### Librerie
- [Sqlite3]
- [Flask]
- [PyPDF2]
- [Datetime]
- [flask_login]
- [jwt]
- [functiontools]

### DataBase
Abbiamo realizzato un DATABASE in SQLITE per la gestione delle offerte(Creazione, Visualizzazione, Ricerca, ecc..), per il login , per l'inserimento di un nuovo utente e/o azienda e per lo storico dei reclami.
[DB](https://github.com/lorisiaco/ProgeIDS/blob/main/jobs.db).

## Funzionalità
- [Registrazione Profilo]
- [Login Profilo]
- [Creazione Offerte]
- [Pubblicazione Offerte]
- [Visualizzazine Candidati]
- [Visualizzazione Offerte]
- [Accettare/Rifiutare Offerte]
- [Ricerca Offerte tramite Keyword]
- [Candidatura Offerte]
- [Effettuare Reclami]

## Componenti del gruppo
- [__Andrea Moressa__](https://github.com/morex5ound)
- [__Loris Iacoban__](https://github.com/lorisiaco)
- [__Amin Borqal__](https://github.com/aminb00)
