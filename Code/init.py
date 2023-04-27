from flask import Flask,flash, render_template, request, redirect, url_for, session
import Offerta
from JobDatabase import JobData 
import sqlite3
import Utente
import Azienda
import PyPDF2
from datetime import timedelta
app = Flask(__name__)
#Impost0 la chiave segreta per la sessione
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.permanent_session_lifetime=timedelta(days=5)

conn = sqlite3.connect('jobs.db' , check_same_thread=False)
cursor = conn.cursor()

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


@app.route('/register', methods=['POST'])
def register():
    # Recupera i dati del modulo di registrazione
    cf = request.form('cf')
    password = request.form('password')
    nome=request.form('nome')
    etá = request.form('etá')
    sesso=request.form('sesso')
    residenza=request.form('residenza')
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
        session.permanent= True
        # Esegue una query per verificare che le credenziali siano corrette
        cursor.execute("SELECT * FROM Utenti WHERE Email=? AND Password=?", (request.form['Email'], request.form['password']))
        user = request.form['Email']
        session["user"]=user
        return redirect(url_for("user",usr=user))
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
    results = None
    if request.method == 'POST':
        # Recupero i parametri di ricerca dal form
        # Eseguo la query sul database
        search_term = request.form.get('search_term')
        search_luogo = request.form.get('search_luogo')
        results = JobData('jobs.db').get_offers_res(search_term,search_luogo)
    return render_template('RicercaOfferta.html', results=results)

@app.route('/RicercaOffertaS', methods=['GET', 'POST'])
def RicercaOffertaS():
    results = None
    if request.method == 'POST':
        # Recupero i parametri di ricerca dal form
        # Eseguo la query sul database
        search_sal = request.form.get('search_sal')
        search_l = request.form.get('search_l')
        results = JobData('jobs.db').get_offers_sal(search_sal,search_l)
    return render_template('RicercaOffertaS.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)