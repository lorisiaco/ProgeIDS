from flask import Flask,flash, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, IntegerField, RadioField
from wtforms.validators import InputRequired, Email, Length
import werkzeug 

import Offerta
from JobDatabase import JobData 
import sqlite3
import Utente
import Azienda

app = Flask(__name__)
#Impost0 la chiave segreta per la sessione
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

conn = sqlite3.connect('jobs.db' , check_same_thread=False)
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template("home.html")
    
@app.route('/Contatti')
def Contatti():
    return render_template("contatti.html")

class Utente(FlaskForm):
    resume = FileField('Curriculum')
    
@app.route('/DashboardUtente')
def DashboardUtente():
    return render_template("DashboardUtente.html")

@app.route('/DashboardAzienda')
def DashboardAzienda():
    return render_template("DashboardAzienda.html")

class RegisterForm(FlaskForm):
    cf = StringField('CF', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])
    nome = StringField('Nome', validators=[InputRequired()])
    eta = IntegerField('Eta', validators=[InputRequired()])
    sesso = RadioField('Sesso', choices=[('maschio', 'Maschio'), ('femmina', 'Femmina')])
    residenza = StringField('Residenza', validators=[InputRequired()])
    resume = FileField('Curriculum')

@app.route('/sign-up',methods=['GET','POST'])
def sign_up():
    form = RegisterForm()
    if form.validate_on_submit():
        # Estrai i dati dal modulo di form
        cf=form.cf.data
        email = form.email.data
        password = form.password.data
        nome = form.nome.data
        eta = form.eta.data
        sesso = form.sesso.data
        residenza=form.residenza.data
        file = form.resume.data
        # Salva il file nella cartella statica del tuo progetto
        file.save('ProgeIDS/Code/static/resumes/{}'.format(file.filename))
        # Crea una nuova istanza dell'utente con tutti i dati del modulo di form e il percorso del file del curriculum
        new_utente = Utente(cf,email,password,nome,eta,sesso,residenza, resume_path='ProgeIDS/Code/static/resumes/{}'.format(file.filename))
        # Salva l'utente nel database o dove preferisci
        db = JobData('jobs.db')
        db.add_ut(new_utente)
    return render_template('sign_up2.html', form=form)

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
        # Esegue una query per verificare che le credenziali siano corrette
        cursor.execute("SELECT * FROM Utenti WHERE Email=? AND Password=?", (request.form['Email'], request.form['password']))
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
    return redirect(url_for('DashboardUtente'))

@app.route('/logout')
def logout():
    # Rimuove la variabile di sessione per indicare che l'utente non è più autenticato
    session.pop('logged_in', None)
    # Redirect alla pagina di login
    return redirect(url_for('login'))

@app.route('/index')
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