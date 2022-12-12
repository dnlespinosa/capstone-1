# from flask_bcrypt import Bcrypt 
from flask_sqlalchemy import SQLAlchemy

# bycrpt = Bcrypt()
db = SQLAlchemy()

class Test(db.Model): 
    tablename = 'Test Table'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)

class User_Info(db.Model):
    tablename = 'User Information'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, primary_key=True)
    password = db.Column(db.Text, primary_key=True)

class user_loadout(db.Model):
    tablename = 'User Loadout'

    # come back to USER ID
    loadout_id = db.Column(db.Integer, primary_key=True)
    loadout_name = db.Column(db.Text, nullable=False)
    loadout_cost = db.Column(db.Integer, primary_key=True)
    # come back to foriegn key selected weapons id 

# class selected_weapons(db.Model):
#     tablename = 'Selected Weapons Arrays'

#     # set a selected_weapons foreign key with user_loadout 
#     # selected_weapons = db.Column(db.JSON, nullable=False)

class weapon_list(db.Model):
    tablename = 'Avaliable Weapons'
    
    weapon_id = db.Column(db.Integer, primary_key=True)
    weapon_name = db.Column(db.Text, nullable=False)
    weapon_cost = db.Column(db.Integer, primary_key=True)
    weapon_img = db.Column(db.Text, primary_key=True)


def connect_db(app):
    db.app = app
    db.init_app(app)