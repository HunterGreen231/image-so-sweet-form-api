from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_heroku import Heroku
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import config

app = Flask(__name__)
heroku = Heroku(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://lnazpnaoydrswi:5de9beb4ee2d75dce60631d9c7273cb77444e619525d7f7a471a6654f39a8164@ec2-75-101-147-226.compute-1.amazonaws.com:5432/dbtlkhnfral2gu"

CORS(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class CData(db.Model):
    __tablename__ = "CustomerDataTable"
    id = db.Column(db.Integer, primary_key=True)
    customer_first_name = db.Column(db.String(30), nullable=False)
    customer_last_name = db.Column(db.String(30), nullable=False)
    customer_email = db.Column(db.String(50), nullable=False)

    def __init__(self, customer_first_name, customer_last_name, customer_email):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name
        self.customer_email = customer_email

class CDataSchema(ma.Schema):
    class Meta:
        fields = ("id", "customer_first_name", "customer_last_name", "customer_email")


customer_data_schema = CDataSchema()
customers_data_schema = CDataSchema(many=True)

@app.route("/customers", methods=["GET"])
def get_customers():
    all_customers = CData.query.all()
    result = customers_data_schema.dump(all_customers)

    return jsonify(result.data)

@app.route("/customer/<id>", methods=["DELETE"])
def delete_customer(id):
    record = CData.query.get(id)
    db.session.delete(record)
    db.session.commit()
    return jsonify("Record deleted")

@app.route("/email-form", methods=["POST"])
def email():

    childs_name = request.json["childsName"]
    email = request.json["email"]
    fantasy_theme = request.json["fantasyTheme"]
    first_name = request.json["firstName"]
    last_name = request.json["lastName"]
    location = request.json["location"]
    customer_message = request.json["message"]
    phone_number = request.json["phoneNumber"]
    referred_by = request.json["referredBy"]

    joined_childs_name = ''.join(childs_name)
    joined_email = ''.join(email)
    joined_fantasy_theme = ''.join(fantasy_theme)
    joined_first_name = ''.join(first_name)
    joined_last_name = ''.join(last_name)
    joined_location = ''.join(location)
    joined_customer_message = ''.join(customer_message)
    joined_phone_number = ''.join(phone_number)
    joined_referred_by = ''.join(referred_by)

    content = (f'''
<b>First Name</b>:    {joined_first_name}<br/><br/>
<b>Last Name</b>:     {joined_last_name}<br/><br/>
<b>Childs Name</b>:   {joined_childs_name}<br/><br/>
<b>Email</b>:         {joined_email}<br/><br/>
<b>Phone Number</b>:  {joined_phone_number}<br/><br/>
<b>Location</b>:      {joined_location}<br/><br/>
<b>Fantasy Theme</b>: {joined_fantasy_theme}<br/><br/>
<b>Referred By</b>:   {joined_referred_by}<br/><br/>
<b>Message</b>:       {joined_customer_message}<br/><br/>
''')

    # message = Mail(
    #     from_email="image-so-sweet-website@gmail.com",
    #     to_emails='webdev.huntergreen@gmail.com',
    #     subject=(f'{joined_first_name} {joined_last_name}'),
    #     html_content=content)
    # try:
    #     sg = SendGridAPIClient(config.SENDGRID_API_KEY)
    #     response = sg.send(message)
    #     print(response.status_code)
    #     print(response.body)
    #     print(response.headers)
    # except Exception as e:
    #     print(e)


    all_CData = Cdata.query.all()

    print("All CData", all_CData)

    # record = CData(joined_first_name, joined_last_name, joined_email)

    # db.session.add(record)
    # db.session.commit()

    return "Sucess!"


if __name__ == "__main__":
    app.debug = True
    app.run()