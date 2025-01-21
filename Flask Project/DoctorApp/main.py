from flask import Flask, render_template


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/error")
def error():
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
