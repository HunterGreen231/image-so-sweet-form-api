from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_heroku import Heroku
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import config

# class CustomerData(db.Model):
#     __tablename__ = "CustomerData"
#     id = db.Column(db.Integer, primary_key=True)
#     customer_name = db.Column(db.String(30), nullable=False)
#     customer_email = db.Column(db.String(50), nullable=False, unique=True)

#     def __init__(self, customer_name, customer_email):
#         self.customer_name = customer_name
#         self.customer_email = customer_email

@app.route("/email-form", methods=["POST"])
def email():
    print(request.json)

    childsName = request.json["childsName"]
    email = request.json["email"]
    fantasyTheme = request.json["fantasyTheme"]
    firstName = request.json["firstName"]
    lastName = request.json["lastName"]
    location = request.json["location"]
    customerMessage = request.json["message"]
    phoneNumber = request.json["phoneNumber"]
    referredBy = request.json["referredBy"]

    content = (f'''
Name:  {firstName}<br/>
Last Name: {lastName}<br/>
Childs Name: {childsName}<br/>
Email: {email}<br/>
Phone Number: {phoneNumber}<br/>
Location: {location}<br/>
Fantasy Theme: {fantasyTheme}<br/>
Referred By: {referredBy}<br/>
Message: {customerMessage}<br/>
''')

    # message = Mail(
    #     from_email="image-so-sweet-website@gmail.com",
    #     to_emails='webdev.huntergreen@gmail.com',
    #     subject=(f'{firstName} {lastName}'),
    #     html_content=content)
    # try:
    #     sg = SendGridAPIClient(config.SENDGRID_API_KEY)
    #     response = sg.send(message)
    #     print(response.status_code)
    #     print(response.body)
    #     print(response.headers)
    # except Exception as e:
    #     print(e)

    return request

if __name__ == "__main__":
    app.debug = True
    app.run()