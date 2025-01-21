from flask import Flask, render_template

app = Flask(__name__)


n = 1


@app.route("/")
def index():
    name = "Ashok"
    global n
    n += 1
    return render_template("index.html", nm=name, num=n)


if __name__ == "__main__":
    app.run(debug=True)
