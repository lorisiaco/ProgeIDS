# Software Architecture
Abbiamo pensato che per il nostro progetto affinche lo sviluppo sia ottimale, non incasinato e semplice il miglior stile architetturale sia quello di tipo 'Model-View-Controller’.

![X.png](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/1200px-MVC-Process.svg.png)

Svilupperemo la nostra web app con :
- `Controller` e `Model`, vengono gestiti dal backend che si occupa di astrarre e manipolare i dati presenti nel database e di gestire le richieste delle funzioni.
- `View` per la visualizzazione dei risultati è gestita dalla parte di frontend attraverso la libreria Flask di Python, Javascript e HTML

## Viste Architetturali
L’architettura del sistema è descritta attraverso 5 diagrammi UML:
- `Use Case Diagram` utilizzato per la descrizione della varie funzione che possono effettuare gli attori del sistema.
- `Class Diagram` utilizzato per la descrizione delle varie classi,metodi, ttributi che compongono la nostra web-app e come interagiscono fra di loro
- `State Machine Diagram` utilizzato per la descrizione dei vari stati che un utente percorre dalla candidatura alla comunica della selezione e i vari stati che un'azienda percorre dalla pubblicazione dell'offerta alla selezione del candidato.
- `Sequence Diagram` utilizzato per la descrizione del processo di inserimento di un'offerta
- `Activity Diagram` utilazzato per la descrizione delll'attività della nostra web-app dalla ricerca offerta dell'utente alla selezione candidato dell'azienda

