from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sampledb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)  # Database Init.


# Database Model
class studinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    sub = db.Column(db.String(20))
    city = db.Column(db.String(20))


# Database Create
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nm = request.form["name"]
        sub = request.form["sub"]
        ct = request.form["city"]

        stdata = studinfo(name=nm, sub=sub, city=ct)
        db.session.add(stdata)
        db.session.commit()
        print("Record Inserted!")
    return render_template("index.html")


@app.route("/showdata")
def showdata():
    stdata = studinfo.query.all()
    return render_template("showdata.html", data=stdata)


if __name__ == "__main__":
    app.run(debug=True)
