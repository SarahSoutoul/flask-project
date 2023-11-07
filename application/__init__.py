import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Create the server
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dzikkayj:EXJlR09usccrJ7xMjKhQpqxWt75PwL-t@trumpet.db.elephantsql.com/dzikkayj"
db = SQLAlchemy(app)

from application import routes