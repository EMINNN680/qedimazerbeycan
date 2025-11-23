from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

class Telebe(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   ad = db.Column(db.String(100), nullable=False)
   yas = db.Column(db.Integer, nullable=False)
def __repr__(self):
   return f"<Telebe {self.ad}>"

messages = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/abideler')
def abideler():
    return render_template("abideler.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        email = request.form.get("email","").strip()
        message = request.form.get("message","").strip()
        name = request.form.get("name","").strip()

        if not name:
            flash("Adı daxil etməmisiniz!", "error")
            return redirect(url_for("contact"))
        if not email:
            flash("E-Poçtunuzu daxil etməmisiniz!", "error")
            return redirect(url_for("contact"))
        if not message:
            flash("Mesajınızı daxil etməmisiniz!", "error")
            return redirect(url_for("contact"))

        messages.append({"name": name, "email": email, "message": message})
        flash("Mesajınız uğurla göndərildi!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", messages=messages)

@app.route('/telebe_form', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        ad = request.form.get("ad", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not ad or not email or not password:
            flash("Xahiş edirik email, şifrə və adınızı daxil edin!", "error")
            return redirect(url_for("register"))

        user = Telebe(username=ad, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        session['username'] = ad
        flash(f"Xoş gəlmisiniz, {ad}!", "success")
        return redirect(url_for("index"))
    return render_template("register.html")

@app.route("/salamla", methods=["POST"])
def salamla():
    ad = request.form.get("ad")
    session['ad'] = ad
    return render_template("salamla.html", ad=ad)

@app.route("/user/<ad>")
def user(ad):
    return render_template("user.html", ad=ad)

@app.route("/elave-et", methods=["GET", "POST"])
def elave_et():
  if request.method == "POST":
    ad = request.form["ad"]
    yas_str = request.form.get("yas", "").strip()

    if yas_str.isdigit():
       yas = int(yas_str)
    else:
       return render_template("error.html", message="Bütün Formları Doldurun!")
    yeni_telebe = Telebe(ad=ad, yas=yas)
    db.session.add(yeni_telebe)
    db.session.commit()
    return redirect(url_for("siyahi"))
  return render_template("form2.html")

@app.route("/siyahi")
def siyahi():
   telebeler = Telebe.query.all()
   return render_template("siyahi.html", telebeler=telebeler)

@app.route("/telebe-form")
def telebe_form():
   return render_template("form2.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)