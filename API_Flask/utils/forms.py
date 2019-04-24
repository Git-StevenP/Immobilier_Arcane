from wtforms import Form, StringField, SelectField, SubmitField, TextAreaField, DecimalField
from utils import bdd
mongo = bdd.MongoDB("Arcane_Immobilier")

# Formulaire de modification du profil
class ProfileEditor(Form):
    last_name = StringField('', render_kw={"placeholder": "Nom"})
    first_name = StringField('', render_kw={"placeholder": "Prénom"})
    birth_date = StringField('', render_kw={"placeholder": "Date de naissance"})

# Formulaire de modification/ajout d'un bien immobilier
class RealEstateEditor(Form):
    # Création de tous les champs du formulaire (nom, description, type de bien, ville, pièces, 
    # caractéristiques des pièces(type de pièce, surface, meublé ou non), propriétaire du bien)

    name = StringField('', render_kw={"placeholder": "Nom"})
    description = TextAreaField('', render_kw={"placeholder": "Description"})
    real_estate_type = SelectField(u'Type de bien', choices=[('maison', 'Maison'), ('appt', 'Appartement'), ('villa', 'Villa')])
    city = StringField('', render_kw={"placeholder": "Ville"})

    # On itère sur 100 champs de pièces (valeur arbitraire par défaut)
    for nb in range(100):

        # Création de variables comportant un nom de variable généré en fonction de l'itération de la boucle
        # room_type0, room_type1, room_type2...
        type_name = 'room_type' + str(nb)
        # room_area0, room_area1, room_area2...
        area_name = 'room_area' + str(nb)
        # room_furniture0, room_furniture1, room_furniture2...
        furniture_name = 'room_furniture' + str(nb)

        # Utilisation de la fonction exec afin d'affecter la même valeur de retour cad un champ du formulaire pour chaque
        # trio de variables précédemment créé (room_type0, room_area0, room_furniture0 => 3 champs, room_type1, room_area1, room_furniture1 => 3 champs)
        exec(type_name + " = SelectField(u'Type de pièce', choices=[('bedroom', 'Chambre'), ('living-room', 'Pièce à vivre'), ('WC', 'Toilettes'), ('bathroom', 'Salle de Bain'), ('office', 'Bureau'), ('kitchen', 'Cuisine'), ('garden', 'Jardin')])")
        exec(area_name + " = DecimalField('', render_kw={'placeholder': 'Surface (en m²)'})")
        exec(furniture_name + " = SelectField(u'Meublé', choices=[('oui', 'Oui'), ('non', 'Non')])")

    owner = StringField('', render_kw={"placeholder": "Propriétaire"})

    def get_rooms_field_list_dict(self, room_number):
        """Retourne la liste des champs du formulaire correspondant aux pièces ainsi que le dictionnaire associé.

        Paramètres nommés :
        self -- le formulaire lui même
        room_number -- le nombre de pièces qu'il faudra retourner

        """

        # Initialisation des deux variables de retour
        roomsFieldList = []
        roomsDict = {}

        # Pour chaque pièce
        for elt in range(room_number):

            # Récupération de l'attribut des champs du formulaire
            room_type_field = getattr(self, 'room_type' + str(elt))
            room_area_field = getattr(self, 'room_area' + str(elt))
            room_furniture_field = getattr(self, 'room_furniture' + str(elt))

            # Ajout de ces champs dans la liste de champs
            roomsFieldList.append({'room_type' : room_type_field, 'room_area' : room_area_field, 'room_furniture' : room_furniture_field})

            # Récupération de la valeur des différents champs du formulaire
            room_type_input = room_type_field.data
            room_area_input = room_area_field.data
            room_furniture_input = room_furniture_field.data

            # Si la valeur est déjà présente dans le dictionnaire
            if 'room_' + str(elt) not in roomsDict:
                roomsDict['room_' + str(elt)] = {"room_type" : str(room_type_input), "room_area" : str(room_area_input), "room_furniture" : room_furniture_input}
            else:
                roomsDict['room_' + str(elt+1)] = {"room_type" : str(room_type_input), "room_area" : str(room_area_input), "room_furniture" : room_furniture_input}
            
            # Ajout du nombre de pièces total dans le dictionnaire
            roomsDict['room_number'] = room_number
        
        return roomsFieldList, roomsDict

# Formulaire de recherche par ville d'un bien
class RealEstateSearch(Form):
    search = StringField('', render_kw={"placeholder": "Chercher par ville..."})
