from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def prva_stran():
    return render_template ("prva_stran.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


if __name__ == '__main__':
    app.run()

