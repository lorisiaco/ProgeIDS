# ProgeIDS
![alt text]()

Scopo del progetto è quello di creare una webapp che permetta di connettere i singoli individui che cercano lavoro con le aziende che hanno delle posizioni libere da riempire.
## Documentazione
La seguente documentazione comprende i documenti realizzati per la progettazione del problema, verranno prima elencati i diagrammi delle classi in UML poi la documentazione del codice (javadoc).

### ANALISI REQUISITI
Dopo un' attenta analisi dei requisiti abbiamo identificato:
- [REQUISITI](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/SoftwareRequirementEngineering.md)

### UML
Abbiamo realizzato i vari diagrammi grazie a STARUML.
Sono nella cartella [Documentazione/Diagrammi](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML)
- [CASI D'USO](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/UseCaseDiagram/UseCaseDiagram.png)
- [ATTIVITÀ](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/ActivityDiagram/ActivityDiagram.png)
- [CLASSI](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/ClassDiagram/ClassDiagram.png)
- [STATE MACHINE AZIENDA](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/StateMachineDiagram/StateMachineDiagramAzienda.png)
- [STATE MACHINE UTENTE](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/StateMachineDiagram/StateMachineDiagramUtente.png)
- [SEQUENZE](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML/SequenceDiagramDiagram/SequenceDiagram.png))

### JavaDoc
- [JAVADOC](https://github.com/lorisiaco/ProgeIDS/blob/main/Documetations/UML)

### Librerie
- [java.awt.BorderLayout] è un layout manager che organizza i componenti all'interno di un contenitore in cinque aree: nord, sud, est, ovest e centro.
- [java.awt.EventQueue] è una classe che gestisce gli eventi in un thread separato, garantendo che gli eventi vengano gestiti in modo sincrono e senza interferenze.
- [java.awt.GridLayout] è un layout manager che organizza i componenti all'interno di un contenitore in una griglia di righe e colonne.
- [java.awt.event.ActionEvent] è un evento generato quando viene eseguita un'azione, ad esempio quando un pulsante viene premuto.
- [java.awt.event.ActionListener] è un'interfaccia che deve essere implementata da un oggetto che desidera ricevere e gestire eventi di azione.
- [java.sql.Connection] rappresenta una connessione a un database relazionale e consente di eseguire operazioni di lettura e scrittura sui dati del database.
- [java.sql.DriverManager] è una classe che gestisce la connessione ai driver del database e consente di ottenere una connessione a un database specifico.
- [java.sql.ResultSet] rappresenta un insieme di risultati di una query SQL e consente di accedere ai dati restituiti dal database.
- [java.sql.SQLException] è un'eccezione che viene generata quando si verifica un errore durante l'esecuzione di un'operazione sul database.
- [java.sql.Statement] rappresenta un'istruzione SQL da eseguire sul database e consente di eseguire query e aggiornamenti sui dati.
- [javax.swing.JButton] è un componente Swing che rappresenta un pulsante cliccabile che può essere utilizzato per avviare azioni.
- [javax.swing.JFrame] è un contenitore Swing che rappresenta una finestra dell'applicazione.
- [javax.swing.JLabel] è un componente Swing che visualizza un'etichetta di testo.
- [javax.swing.JOptionPane] è una finestra di dialogo Swing che visualizza un messaggio e consente all'utente di selezionare una risposta.
- [javax.swing.JPanel] è un contenitore Swing che può essere utilizzato per organizzare i componenti all'interno di un'interfaccia utente.
- [javax.swing.JPasswordField] è un componente Swing che permette di inserire una password in modo sicuro.
- [javax.swing.JTextField] è un componente Swing che permette di inserire testo.

### Jars
I seguenti jar sono stati utilizzati per la consegna del progetto, permettono quindi il lancio dell'applicazione secondo le funzionalità descritte nell'introduzione..

### DataBase
Abbiamo realizzato un DATABASE in mysql per la gestione delle offerte, per il LOGIN e l'inserimento di un nuovo utente.
[DB](Code/__pycache__/JobDatabase.cpython-310.pyc).

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
- [__Amin Borqal__](https://github.com/)
