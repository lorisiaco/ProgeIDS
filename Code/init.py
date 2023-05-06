from flask import Flask,flash, render_template, request, redirect, url_for, session,jsonify, make_response
import Offerta
from JobDatabase import JobData 
import sqlite3
import Utente
import Azienda
import PyPDF2
from datetime import timedelta
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import jwt
from datetime import datetime, timedelta
from functools import wraps


app = Flask(__name__)
#Impost0 la chiave segreta per la sessione
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.permanent_session_lifetime=timedelta(minutes=1)

conn = sqlite3.connect('jobs.db' , check_same_thread=False)
cursor = conn.cursor()

def token_required(func):
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401

        try:

            data = jwt.decode(token, app.config['SECRET_KEY'])
        # You can use the JWT errors in exception
        # except jwt.InvalidTokenError:
        #     return 'Invalid token. Please log in again.'
        except:
            return jsonify({'Message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return decorated



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/c')
def c():
    job_offers = JobData('jobs.db').get_offers()
    return render_template('prova3.html', job_offers=job_offers)

@app.route('/a', methods=['POST'])
def a():
    offerta_id2 = request.form['offerta_id2']
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("SELECT id_ca FROM Candidature WHERE id_offerta = ?", (offerta_id2,))
    prescelto = c.fetchone()
    conn.close()
    if prescelto:
        return "La persona selezionata è la persona con questo Codice Fiscale: " + str(prescelto[0])
    else:
        return "Nessuna persona è stata prescelta per questa offerta di lavoro."

@app.route('/candidati', methods=['POST'])
def candidati():
    # Recupera i dati della candidatura dalla richiesta
    offerta_id = request.form['offerta_id']
    utente_cf = request.form['utente_cf']
    # Salva i dati della candidatura nel database
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Candidature (idc INTEGER PRIMARY KEY AUTOINCREMENT, id_offerta TEXT, id_utente TEXT, id_ca INTEGER, FOREIGN KEY (id_offerta) REFERENCES OfferteLavoro (ID), FOREIGN KEY (id_utente) REFERENCES Utente(CF));')
    c.execute("INSERT INTO Candidature (id_offerta, id_utente) VALUES (?, ?)", (offerta_id, utente_cf))
    conn.commit()
    conn.close()
    return "Candidatura inviata con successo!"

@app.route('/CandidatoSelezionato', methods=['POST'])
def CandidatoSelezionato():
    utente_id = request.form['utente_id']
    offerta_id1 = request.form['offerta_id1']
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("UPDATE Candidature SET id_ca = ? WHERE id_offerta = ?", (utente_id, offerta_id1))
    conn.commit()
    conn.close()
    return "Candidato selezionato con successo!"


@app.route('/VisualizzaCandidati', methods=['GET','POST'])
def VisualizzaCandidati():
    if request.method == 'POST':
        offerta_id = request.form['offerta_id']
    else:
        offerta_id = request.args.get('offerta_id')
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Utenti u JOIN Candidature c on u.CF=c.id_utente WHERE id_offerta= ?",(offerta_id,))
    candidati=c.fetchall()
    if len(candidati) == 0:
        message = "Nessun candidato trovato per l'offerta con id {}".format(offerta_id)
        return render_template('Candidati.html', message=message)
    else:
        return render_template('Candidati.html', candidati=candidati, offerta_id=offerta_id)

@app.route('/Contatti')
def Contatti():
    return render_template("contatti.html")
    
@app.route('/DashboardUtente')
def DashboardUtente():
    job_offers = JobData('jobs.db').get_offers()
    return render_template('DashboardUtente.html', job_offers=job_offers)

@app.route('/DashboardAzienda')
def DashboardAzienda():
    return render_template("DashboardAzienda.html")

@app.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        CF = request.form.get('cf')
        Nome=request.form.get('firstName')
        Etá = request.form.get('etá')
        Sesso=request.form.get('sesso')
        Residenza=request.form.get('residenza')
        Email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        pdf_file = request.files['cv']

        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_content = pdf_reader.pages[0].extract_text()

        if len(Email) < 4:
            flash('Email must be greater than 4 characters.',category='error')
        elif len(Nome) < 2:
            flash('First name must be greater than 1 characters.',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.',category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.',category='error')
        else:
            flash('Account created!',category='success')

        new_utente=Utente.Utente(CF,Email,password1,Nome, Etá,Sesso,Residenza, pdf_content)
        db = JobData('jobs.db')
        db.add_ut(new_utente)
    return render_template('sign_up.html')


@app.route('/sign-up-azienda',methods=['GET','POST'])
def sign_up_azienda():
    if request.method=='POST':
        cf = request.form.get('cf')
        sedelegale=request.form.get('sedelegale')
        email=request.form.get('email')
        nomeazienda=request.form.get('nomeazienda')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.',category='error')
        elif len(nomeazienda) < 2:
            flash('First name must be greater than 1 characters.',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.',category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.',category='error')
        else:
            flash('Account created!.',category='success')

        new_azienda=Azienda.Azienda(email,cf,nomeazienda,sedelegale,password1)
        db = JobData('jobs.db')
        db.add_az(new_azienda)
    return render_template('sign_up_azienda.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
# Esegue una query per verificare che le credenziali siano corrette
    if request.method == 'POST':
        # Verifica se il checkbox in login.html è stato selezionato
        if request.form['checkIfAzienda'] == '':
            cursor.execute("SELECT * FROM Utenti WHERE Email=? AND Password=?", (request.form['Email'], request.form['password']))
            result = cursor.fetchone()
            if result:
                # Imposta la variabile di sessione per indicare che l'utente è autenticato
                session["user"]=request.form['Email']
                return redirect(url_for("user",usr=request.form['Email']))
            else:
                # Messaggio di errore nel caso in cui le credenziali siano errate
                error = "Invalid credentials"
                #mostra il modulo di login piu il messaggio di errore
                return render_template('login.html', error=error)
        else:
            cursor.execute("SELECT * FROM Aziende WHERE Email=? AND Password=?", (request.form['Email'], request.form['password']))
            result = cursor.fetchone()
            if result:
                # Imposta la variabile di sessione per indicare che l'utente è autenticato
                session["user"]=request.form['Email']
                return redirect(url_for("azd",azd=request.form['Email']))
            else:
                # Messaggio di errore nel caso in cui le credenziali siano errate
                error = "Invalid credentials"
                #mostra il modulo di login piu il messaggio di errore
                return render_template('login.html', error=error)
    else:
    # Mostra il modulo di login
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    # Verifica che l'utente sia autenticato
    if "user" in session:
        user= session["user"]
        return render_template('DashboardUtente.html')
    else:
        return redirect(url_for('login'))

@app.route('/<azd>')
def azd():
    # Verifica che l'utente sia autenticato
    if "azd" in session:
        azd= session["user"]
        return render_template('DashboardAzienda.html')
    else:
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    # Rimuove la variabile di sessione per indicare che l'utente non è più autenticato
    session.pop('user', None)
    # Redirect alla pagina di login
    return redirect(url_for('login'))

@app.route('/index')
def index():
    db = JobData('jobs.db')
    jobs = db.get_offers()
    return render_template('index2.html', jobs=jobs)

@app.route('/add', methods=['POST'])
def add_job():
    id= request.form['id']
    ruolo = request.form['ruolo']
    azienda = request.form['azienda']
    luogo = request.form['luogo']
    salario = request.form['salario']
    descrizione = request.form['descrizione']
    job = Offerta.Offerta(id=id, ruolo=ruolo, azienda=azienda, sedelegale=luogo, salario=salario, descrizione=descrizione)
    db = JobData('jobs.db')
    db.add_of(job)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')

def delete_job(id):
    db = JobData('jobs.db')
    db.delete(id)
    return redirect(url_for('index'))

@app.route('/RicercaOfferta', methods=['GET', 'POST'])
def RicercaOfferta():
    results = []
    if request.method == 'POST':
        # Recupero i parametri di ricerca dal form
        # Eseguo la query sul database
        search_term = request.form.get('search_term')
        search_luogo = request.form.get('search_luogo')
        db=JobData('jobs.db')
        results = db.get_offers_res(search_term,search_luogo)
    return render_template('RicercaOfferta.html', results=results)

@app.route('/RicercaOffertaS', methods=['GET', 'POST'])
def RicercaOffertaS():
    results = []
    if request.method == 'POST':
        # Recupero i parametri di ricerca dal form
        # Eseguo la query sul database
        search_sal = request.form.get('search_sal')
        search_l = request.form.get('search_l')
        db=JobData('jobs.db')
        results = db.get_offers_sal(search_sal,search_l)
    return render_template('RicercaOffertaS.html', results=results)
    

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)