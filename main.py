from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def prva_stran():
    return render_template ("prva_stran.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/poslji-sporocilo", methods=["POST"])
def poslji_sporocilo():
    zadeva = request.form.get("zadeva")
    sporocilo = request.form.get("sporocilo")

     # Toukaj bi shranili te spremenjljivki v bazo

    print ("zadeva je: " + zadeva)
    print ("Sporočilo je: " + sporocilo)
    return "Hvala za poslano zadevo: " + zadeva


if __name__ == '__main__':
    app.run()

