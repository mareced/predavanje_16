import random
import uuid
from flask import Flask, render_template, request, redirect, make_response
from modeli import Komentar, db, Uporabnik


app = Flask(__name__)
db.create_all()

@app.route("/")
def prva_stran():
    sejna_vrednost = request.cookies.get("sejna_vrednost")
    uporabnik = db.query(Uporabnik).filter_by(sejna_vrednost=sejna_vrednost).first()
    if uporabnik:
        ime = uporabnik.ime
    else:
        ime = None

    komentarji = db.query(Komentar).all()
    return render_template ("prva_stran.html", ime=ime, komentarji=komentarji)

@app.route("/kontakt")
def kontakt():
    emaili = ["ime@example.com, ime@gmail.com"]
    return render_template("kontakt.html", emaili = emaili)

@app.route("/poslji-sporocilo", methods=["POST"])
def poslji_sporocilo():
    zadeva = request.form.get("zadeva")
    sporocilo = request.form.get("sporocilo")

@app.route("/prijava", methods=["POST"])
def prijava():
    ime=request.form.get("ime")

    sejna_vrednost = str(uuid.uuid4())

    uporabnik = db.query(Uporabnik).filter_by(ime=ime).first()
    if not uporabnik:
        uporabnik = Uporabnik(ime=ime, sejna_vrednost=sejna_vrednost)
    else:
        uporabnik.sejna_vrednost = sejna_vrednost

    db.add(uporabnik)
    db.commit()

    odgovor = make_response(redirect("/"))
    odgovor.set_cookie("sejna_vrednost", sejna_vrednost)
    return odgovor

@app.route("/komentar", methods=["POST"])
def poslji_komentar():
    vsebina_komentarja = request.form.get("vsebina")

    sejna_vrednost = request.cookies.get("sejna_vrednost")
    uporabnik = db.query(Uporabnik).filter_by(sejna_vrednost=sejna_vrednost).first()

    #Tukaj se bo shranil komentar v podatkovno bazo

    komentar = Komentar(
        avtor=uporabnik.ime,
        vsebina=vsebina_komentarja)

    db.add(komentar)

    db.commit()

    return redirect("/")

     # Toukaj bi shranili te spremenjljivki v bazo

    print ("Sporočilo je: " + sporocilo)
    return render_template("zadeva.html", zadeva=zadeva)

@app.route("/skrito_stevilo")
def skrito_stevilo():

    odgovor = make_response(render_template("skrito_stevilo.html"))

    if not request.cookies.get("skritoSteviloPiskot"):
        stevilo = str(random.randint(1, 20))
        odgovor.set_cookie("skritoSteviloPiskot", stevilo)
    return odgovor

@app.route("/poslji-skrito-stevilo", methods=["POST"])
def poslji_skrito_stevilo():
    skrito_stevilo = request.cookies.get("skritoSteviloPiskot")
    vpisano_stevilo =request.form.get("stevilo")
    print(skrito_stevilo, vpisano_stevilo)
    if skrito_stevilo == vpisano_stevilo:
        return "PRAVILNO"
    else:
        return "NI PRAVILNO"


if __name__ == '__main__':
    app.run(debug=True)

