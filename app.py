from flask import Flask, render_template, request, flash, redirect, session, g
from models import db, connect_db, Test

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///CS_go'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = 'its a secret'
# # toolbar = DebugToolbarExtension(app)

connect_db(app)
# WHY DOES THIS WORK?!?!?!
with app.app_context():
    db.create_all()

@app.route('/')
def base_page():
    return render_template('base.html')

@app.route('/test')
def test_db(): 
    # DO NOT USE THIS ROUTE THIS IS JUST TO TEST THE DATABASE CONNECTION 
    test = Test(first_name='Dan')
    db.session.add(test)
    db.session.commit()

    return redirect('/')