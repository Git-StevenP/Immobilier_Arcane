from wtforms import Form, StringField, SelectField, SubmitField
from utils import bdd
mongo = bdd.MongoDB("Arcane_Immobilier")


class ProfileEditor(Form):
    last_name = StringField('', render_kw={"placeholder": "Nom"})
    first_name = StringField('', render_kw={"placeholder": "Prénom"})
    birth_date = StringField('', render_kw={"placeholder": "Date de naissance"})
