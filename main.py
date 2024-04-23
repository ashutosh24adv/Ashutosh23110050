from flask import Flask,render_template,request

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/"
db = SQLAlchemy(app)

class purchase(db.Model):
    sno = db.Column(db.String(10), primary_key=True)
    reference = db.Column(db.String(20),nullable = False)
    journal_data = db.Column(db.String(30),  nullable = False)
    purchase_date = db.Column(db.String(30), nullable = False)
    expiry_date = db.Column(db.String(30))
    purchaser_name = db.Column(db.String(120), nullable = False)
    prefix = db.Column(db.String(10), nullable = False)
    bond_no = db.Column(db.String(10), nullable = False)
    denominations = db.Column(db.String(40), nullable = False)
    branch_code = db.Column(db.String(8), nullable = False)
    issue_teller = db.Column(db.String(14), nullable = False)
    status = db.Column(db.String(20), nullable = False)

class redemption(db.Model):
    sno = db.Column(db.String(10), primary_key=True)
    encashment_date = db.Column(db.String(40),nullable = False)
    party_name = db.Column(db.String(120),  nullable = False)
    account_no = db.Column(db.String(30), nullable = False)
    prefix = db.Column(db.String(30))
    bond_no= db.Column(db.String(10), nullable = False)
    denominations = db.Column(db.String(40), nullable = False)
    branch_code = db.Column(db.String(8), nullable = False)
    pay_teller = db.Column(db.String(20), nullable = False)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)