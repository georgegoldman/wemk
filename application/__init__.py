from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'
app.debug=True

from .views import view
from .auth import auth
app.register_blueprint(view)
app.register_blueprint(auth)