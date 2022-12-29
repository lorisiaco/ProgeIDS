from flask import Flask, render_template, request, redirect, url_for, session
import Offerta
from JobDatabase import JobData 
import sqlite3
import Utente
import Azienda

app = Flask(__name__)
#Impost0 la chiave segreta per la sessione
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

@app.route('/register', methods=['POST'])
def register():
    # Recupera i dati del modulo di registrazione
    cf = request.form['cf']
    password = request.form['password']
    nome=request.form['nome']
    etá = request.form['etá']
    sesso=request.form['sesso']
    residenza=request.form['residenza']
    new_utente=Utente.Utente(cf,password,nome, etá,sesso,residenza)
    db = JobData('jobs.db')
    db.add_ut(new_utente)
    return redirect(url_for('register_success'))

# Gestisce le richieste GET per la pagina di conferma di registrazione
@app.route('/register/success')
def register_success():
    return render_template('register_success.html')

# Gestisce le richieste GET per la pagina di registrazione
@app.route('/register')
def show_register_form():
    return render_template('register.html')

@app.route('/register_azienda', methods=['POST'])
def register_azienda():
    # Recupera i dati del modulo di registrazione
    idc= request.form['idc']
    nome = request.form['nome']
    luogo = request.form['luogo']
    passw = request.form['passw']
    new_azienda=Azienda.Azienda(idc,nome,luogo,passw)
    db = JobData('jobs.db')
    db.add_az(new_azienda)
    return redirect(url_for('register_success'))

# Gestisce le richieste GET per la pagina di registrazione
@app.route('/register_azienda')
def show_register_azienda_form():
    return render_template('registerAzienda.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Esegue una query per verificare che le credenziali siano corrette
        cursor.execute("SELECT * FROM Utenti WHERE id=? AND password=?", (request.form['id'], request.form['password']))
        user = cursor.fetchone()
        if user:
            # Imposta la variabile di sessione per indicare che l'utente è autenticato
            session['logged_in'] = True
            # Redirect alla pagina di benvenuto
            return redirect(url_for('welcome'))
    # Mostra il modulo di login
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    # Verifica che l'utente sia autenticato
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('/'))

@app.route('/logout')
def logout():
    # Rimuove la variabile di sessione per indicare che l'utente non è più autenticato
    session.pop('logged_in', None)
    # Redirect alla pagina di login
    return redirect(url_for('login'))

@app.route('/')
def index():
    db = JobData('jobs.db')
    jobs = db.get_offers()
    return render_template('index.html', jobs=jobs)

@app.route('/add', methods=['POST'])
def add_job():
    id= request.form['id']
    ruolo = request.form['ruolo']
    azienda = request.form['azienda']
    luogo = request.form['luogo']
    salario = request.form['salario']
    descrizione = request.form['descrizione']
    job = Offerta.Offerta(id=id, ruolo=ruolo, azienda=azienda, luogo=luogo, salario=salario, descrizione=descrizione)
    db = JobData('jobs.db')
    db.add_of(job)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_job(id):
    db = JobData('jobs.db')
    db.delete(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)