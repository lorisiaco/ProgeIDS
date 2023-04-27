from flask import Flask,flash, render_template, request, redirect, url_for, session
import Offerta
from JobDatabase import JobData 
import sqlite3
import Utente
import Azienda
import PyPDF2
from datetime import timedelta
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
app = Flask(__name__)
#Impost0 la chiave segreta per la sessione
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.permanent_session_lifetime=timedelta(minutes=1)

conn = sqlite3.connect('jobs.db' , check_same_thread=False)
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template("home.html")
    
@app.route('/Contatti')
def Contatti():
    return render_template("contatti.html")
    
@app.route('/DashboardUtente')
@login_required
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
    if request.method == 'POST':
        session.permanent= True
    #metti un flow control che verifica se si tratta di un utente o di un azienda
    
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
@login_required
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
@login_required
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
@login_required
def delete_job(id):
    db = JobData('jobs.db')
    db.delete(id)
    return redirect(url_for('index'))

@app.route('/RicercaOfferta', methods=['GET', 'POST'])
@login_required
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
@login_required
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