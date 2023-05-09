# Software Testing
Durante lo sviluppo della nostra web-app , nelle parti piu critiche del nostro codice, sopprattutto nel back-end , abbiamo implementato dei unit test per prevenire malfunzionamenti nel codice evitando cosi spiacevoli inconvenienti.
## Libreria di Test
Per lo sviluppo dei nostri test in ambiente python abbiamo utilizzato la libreria *Unittest* e la libreria *Coverage* per il coverage dei test sul codice.
## Elenco Test
Nel file test_last.py ????????  è contenuta la classe **TestJobDatabase** dei nostri unit test. Abbiamo deciso di testare la classe JobData del file JobDatabase.py in quanto per nostra opinione è la classe piu importante e piu critica. Un errore , un malfunzionamento della classe potrebbe causare errori piu grandi nella web-app.
La classe TestJobDatabase è suddivista nei seguenti sotto-test:
- test_get_offers
- test_add_of
- test_delete
- test_add_ut
- ?
- ?

Per poter ripetere i test è necessario eliminare il BD Test1 e per gli ultimi 5 sottotest cambiare la chiave primaria ossia il primo valore (es: email1 ---> email3).

I nostri test sono passati tutti:
Mettere immagine???????
Il nostro coverage è il seguente:
Mettere immagine coverage