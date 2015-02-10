<<<<<<< HEAD
from flask import Flask, session, redirect
from index import index
from login import login
from register import register
from dashboard import dashboard
from video import video
from profile import profile
from api import api
from upload import upload
import config
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')

app = Flask(__name__)
app.secret_key = "HUAa%[3cI76px',Bu}?9nS6~_4x&:{57mBX|FE2p0;<}0fX{E9m695xs`Q(PN}R"
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

port = 5000

app.register_blueprint(api)
app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(dashboard)
app.register_blueprint(video)
app.register_blueprint(profile)
app.register_blueprint(upload)

@app.route("/logout/")
def logout():
    session.pop("login")
    return redirect("/")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=port)
=======
from flask import Flask, session, redirect
from index import index
from login import login
from register import register
from dashboard import dashboard
from video import video
from profile import profile
from api import api
from upload import upload
import config
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')

app = Flask(__name__)
app.secret_key = "HUAa%[3cI76px',Bu}?9nS6~_4x&:{57mBX|FE2p0;<}0fX{E9m695xs`Q(PN}R"
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

port = 5000

app.register_blueprint(api)
app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(dashboard)
app.register_blueprint(video)
app.register_blueprint(profile)
app.register_blueprint(upload)

@app.route("/logout/")
def logout():
    session.pop("login")
    return redirect("/")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=port)
>>>>>>> a662b8352477fdbf4186739144985ab899973242
