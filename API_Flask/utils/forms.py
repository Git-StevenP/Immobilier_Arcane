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
