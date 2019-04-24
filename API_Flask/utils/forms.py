from wtforms import Form, StringField, SelectField, SubmitField, TextAreaField, DecimalField
from utils import bdd
mongo = bdd.MongoDB("Arcane_Immobilier")


class ProfileEditor(Form):
    last_name = StringField('', render_kw={"placeholder": "Nom"})
    first_name = StringField('', render_kw={"placeholder": "Prénom"})
    birth_date = StringField('', render_kw={"placeholder": "Date de naissance"})

class RealEstateEditor(Form):
    name = StringField('', render_kw={"placeholder": "Nom"})
    description = TextAreaField('', render_kw={"placeholder": "Description"})
    real_estate_type = SelectField(u'Type de bien', choices=[('maison', 'Maison'), ('appt', 'Appartement'), ('villa', 'Villa')])
    city = StringField('', render_kw={"placeholder": "Ville"})
    for nb in range(100):
        type_name = 'room_type' + str(nb)
        area_name = 'room_area' + str(nb)
        furniture_name = 'room_furniture' + str(nb)
        exec(type_name + " = SelectField(u'Type de pièce', choices=[('bedroom', 'Chambre'), ('living-room', 'Pièce à vivre'), ('WC', 'Toilettes'), ('bathroom', 'Salle de Bain'), ('office', 'Bureau'), ('kitchen', 'Cuisine'), ('garden', 'Jardin')])")
        exec(area_name + " = DecimalField('', render_kw={'placeholder': 'Surface (en m²)'})")
        exec(furniture_name + " = SelectField(u'Meublé', choices=[('oui', 'Oui'), ('non', 'Non')])")
    owner = StringField('', render_kw={"placeholder": "Propriétaire"})

    def get_rooms_field_list_dict(self, room_number):
        roomsFieldList = []
        roomsDict = {}

        for elt in range(room_number):

            room_type_field = getattr(self, 'room_type' + str(elt))
            room_area_field = getattr(self, 'room_area' + str(elt))
            room_furniture_field = getattr(self, 'room_furniture' + str(elt))

            roomsFieldList.append({'room_type' : room_type_field, 'room_area' : room_area_field, 'room_furniture' : room_furniture_field})

            room_type_input = room_type_field.data
            room_area_input = room_area_field.data
            room_furniture_input = room_furniture_field.data

            if 'room_' + str(elt) not in roomsDict:
                roomsDict['room_' + str(elt)] = {"room_type" : str(room_type_input), "room_area" : str(room_area_input), "room_furniture" : room_furniture_input}
            else:
                roomsDict['room_' + str(elt+1)] = {"room_type" : str(room_type_input), "room_area" : str(room_area_input), "room_furniture" : room_furniture_input}
            
            roomsDict['room_number'] = room_number
        
        return roomsFieldList, roomsDict


class RealEstateSearch(Form):
    search = StringField('', render_kw={"placeholder": "Chercher par ville..."})
