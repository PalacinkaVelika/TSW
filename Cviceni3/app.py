from flask import Flask, render_template, request, session, flash, redirect, url_for, get_flashed_messages, jsonify



app = Flask(__name__, template_folder='templates')
app.secret_key = "asdasdas"


nabidka = [
    {
        "název": "čoky",
        "cena": 123
    },
    {
        "název": "piko",
        "cena": 823
    },
    {
        "název": "weedenska",
        "cena": 66712783
    },
    {
        "název": "kybl",
        "cena": 60
    },
]


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/picy", methods=["GET"])
def picy():
    return render_template("picy.html", nabidka=nabidka)

@app.route("/objednej", methods=["GET","POST"])
def objednej():
    if request.method == "POST":
        nazev = request.form.get("nazev")
        mnozstvi = int(request.form.get("mnozstvi"))
      #  flash(nazev)
      #  flash(mnozstvi)
        celkova_cena = 0
        for pica_z in nabidka:
            if pica_z["název"] == nazev:
                celkova_cena = mnozstvi * pica_z["cena"]
                break
        with open("fakura.txt", "w") as faktura:
            faktura.write(f"Zaplat:{celkova_cena}")
        return redirect("/")
    return render_template("objednej.html")



if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000, debug=True)
    