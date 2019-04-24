# Imports
import pymongo
from flask import Flask, render_template, url_for, request, session, redirect, flash

import config
from utils import bdd, forms

# Initialisation et chargment du fichier Config
app = Flask(__name__)
app.config.from_object(config)

#Initialisation de la base de donnee
mongo = bdd.MongoDB("Arcane_Immobilier")

# Route principale de l'application Flask
@app.route('/', methods=['POST', 'GET'])
def index():
    if 'username' in session:

        mongo.db.room_number.drop()
        mongo.insert_one('room_number', {'number' : 1})

        searchForm = forms.RealEstateSearch(request.form)

        if request.method == 'POST':
            real_estate_list = mongo.db.biens_immobilier.find({'city' : searchForm.search.data})
        else:
            real_estate_list = mongo.db.biens_immobilier.find()

        all_real_estate = []
        for real_estate in real_estate_list:
            all_rooms = []
            for key in real_estate['rooms']:
                if key != 'room_number':
                    all_rooms.append(real_estate['rooms'][key])
            all_real_estate.append({'name' : real_estate['name'], 'description' : real_estate['description'], 'type' : real_estate['type'], 'city' : real_estate['city'], 'owner' : real_estate['owner'], 'rooms' : all_rooms , 'property' : real_estate['property']})
        print(all_real_estate)
        print(session['username'])

        return render_template('home.html', username = session['username'], form=searchForm, all_real_estate = all_real_estate)

    return render_template('index.html')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if 'username' in session:

        users = mongo.db.users

        profileForm = forms.ProfileEditor(request.form)
        searchForm = forms.RealEstateSearch(request.form)

        if request.method == 'POST':
            last_name = profileForm.last_name.data
            first_name = profileForm.first_name.data
            birth_date = profileForm.birth_date.data
            users.update({'username' : session['username']}, {'$set': { 'last_name': last_name, 'first_name' : first_name, 'birth_date' : birth_date } })
            return render_template('home.html', username = session['username'], form=searchForm)

        return render_template('profile.html', username = session['username'], profileForm = profileForm)

    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    if 'username' in session:

        realEstateForm = forms.RealEstateEditor(request.form)
        searchForm = forms.RealEstateSearch(request.form)

        number_collection = mongo.db.room_number
        room_number = number_collection.find_one()['number']

        roomsFieldList, roomsDict = realEstateForm.get_rooms_field_list_dict(room_number)

        if request.method == 'POST':

            if request.form.get('ajouter'):
                number_collection.update_many({}, {'$set' : {'number' :  room_number + 1}})

                return redirect(url_for('add'))

            if request.form.get('retirer'):
                number_collection.update_many({}, {'$set' : {'number' :  room_number - 1}})

                return redirect(url_for('add'))

            if request.form.get('modifier'):

                result = {}

                result['name'] = realEstateForm.name.data
                result["description"] = realEstateForm.description.data
                result["type"] = realEstateForm.real_estate_type.data
                result['city'] = realEstateForm.city.data
                result['rooms'] = roomsDict
                result['owner'] = realEstateForm.owner.data
                result['property'] = session['username']

                mongo.insert_one('biens_immobilier', result)

                return render_template('home.html', username = session['username'], form=searchForm)

        return render_template('add.html', username = session['username'], form = realEstateForm, roomsFieldList = roomsFieldList)

    return render_template('index.html')

@app.route('/modify/<real_estate>', methods=['POST', 'GET'])
def modify(real_estate):
    if 'username' in session:

        realEstateForm = forms.RealEstateEditor(request.form)
        searchForm = forms.RealEstateSearch(request.form)

        real_estate_collection = mongo.db.biens_immobilier
        room_number = real_estate_collection.find_one({'name' : real_estate})['rooms']['room_number']

        roomsFieldList, roomsDict = realEstateForm.get_rooms_field_list_dict(room_number)
        
        if request.method == 'POST':

            if request.form.get('ajouter'):
                mongo.update_real_estate(real_estate, 'rooms', {'room_number' :  room_number + 1})

                return redirect(url_for('modify', real_estate=real_estate))

            if request.form.get('retirer'):
                mongo.update_real_estate(real_estate, 'rooms', {'room_number' :  room_number - 1})

                return redirect(url_for('modify', real_estate=real_estate))

            if request.form.get('modifier'):

                if realEstateForm.name.data:
                    mongo.update_real_estate(real_estate, 'name', realEstateForm.name.data)
                    real_estate = realEstateForm.name.data

                mongo.update_real_estate(real_estate, 'description', realEstateForm.description.data)
                mongo.update_real_estate(real_estate, 'type', realEstateForm.real_estate_type.data)
                mongo.update_real_estate(real_estate, 'city', realEstateForm.city.data)
                mongo.update_real_estate(real_estate, 'rooms', roomsDict)
                mongo.update_real_estate(real_estate, 'owner', realEstateForm.owner.data)
                
                return render_template('home.html', username = session['username'], form=searchForm)

        return render_template('modify.html', username = session['username'], form = realEstateForm, roomsFieldList = roomsFieldList)

    return render_template('index.html')


# Route d'inscription des utilisateurs
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            users.insert({'username' : request.form['username'], 'password' : request.form['pass']})
            session['username'] = request.form['username']
            return redirect('/')

        return redirect('/error_register')

    return render_template('register.html')

# Route de connexion des utilisateurs
@app.route('/login',methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username' : request.form['username']})

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
