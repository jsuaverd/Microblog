from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)


#crating an instance of SQLALchemy class
db = SQLAlchemy(app)

#creating a migration object that associates app and db
migrate = Migrate(app,db)


from app import routes, models
