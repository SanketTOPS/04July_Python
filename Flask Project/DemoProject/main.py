from flask import Flask

app = Flask(__name__)  # App initlization


@app.route("/")
def index():
    return "Hello Flask!"


@app.route("/about")
def about():
    return "This is About Screen!"


@app.route("/contact")
def contact():
    return "This is Contact Page!"


if __name__ == ("__main__"):
    # app.run()
    app.run(debug=True)
