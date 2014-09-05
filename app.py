from flask import Flask, session, redirect
from index import index
from login import login
from register import register
from dashboard import dashboard
from video import video
import config

app = Flask(__name__)
app.secret_key = "HUAa%[3cI76px',Bu}?9nS6~_4x&:{57mBX|FE2p0;<}0fX{E9m695xs`Q(PN}R"
app.debug = True
port = 5000

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(dashboard)
app.register_blueprint(video)

@app.route("/logout/")
def logout():
    session.pop("login")
    return redirect("/")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=port)