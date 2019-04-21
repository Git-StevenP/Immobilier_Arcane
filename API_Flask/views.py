# Imports
import pymongo
from flask import Flask, render_template, url_for, request, session, redirect, flash

import config
from utils import bdd

# Initialisation et chargment du fichier Config
app = Flask(__name__)
app.config.from_object(config)

#Initialisation de la base de donnee
mongo = bdd.MongoDB("Arcane_Immobilier")

# Route principale de l'application Flask
@app.route('/', methods=['POST', 'GET'])
def index():
    if 'username' in session:

        return render_template('home.html')

    return render_template('index.html')

# Route d'inscription des utilisateurs
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            users.insert({'name' : request.form['username'], 'password' : request.form['pass']})
            session['username'] = request.form['username']
            return redirect('/')

        return redirect('/error_register')

    return render_template('register.html')

# Route de connexion des utilisateurs
@app.route('/login',methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user :
        if (request.form['pass'].encode('utf-8') == login_user['password'].encode('utf-8')):
            session['username'] = request.form['username']
            return redirect('/')

    return redirect('/error_login')

# Route d'erreur d'inscription
@app.route('/error_register')
def error_register():
    return render_template('error_register.html')

# Route d'erreur de connexion
@app.route('/error_login')
def error_login():
    return render_template('error_login.html')

# Route de deconnexion de l'utilisateur
@app.route('/deco')
def deconnection():
    del session['username']
    return redirect('/')
