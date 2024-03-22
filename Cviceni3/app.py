from flask import Flask, render_template, request, session, flash, redirect, url_for, get_flashed_messages, jsonify, make_response
import json


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

@app.route("/api/picy", methods=["GET"])
def api_get_picy():
    return make_response(json.dumps(nabidka), 200)

@app.route("/api/pica", methods=["GET"])
def api_get_pica():
    nazev = request.args.get("jmeno")
    # Check if the name parameter is provided
    if not nazev:
        return jsonify({"error": "Parameter 'jmeno' is missing"}), 400
    # Search for the pizza in the menu
    selected_pizza = None
    for pizza in nabidka:
        if pizza["název"] == nazev:
            selected_pizza = pizza
            break
    if selected_pizza:
        return jsonify(selected_pizza), 200
    else:   
        return jsonify({"error": f"Pizza '{nazev}' not found"}), 404

@app.route("/api/pica", methods=["POST"])
def api_post_picy():
    nazev = request.args.get("jmeno")
    cena = request.args.get("cena")
    if not nazev or not cena:
        return jsonify({"error": "Parameter 'jmeno' or 'cena' is missing"}), 400
    else:
        nova_pizza = {nazev : cena}
        nabidka.append(nova_pizza)
        return jsonify(nova_pizza), 200
    
@app.route("/api/pica", methods=["PUT"])
def api_put_picy():
    nazev = request.args.get("jmeno")
    cena = request.args.get("cena")
    if not nazev or not cena:
        return jsonify({"error": "Parameter 'jmeno' or 'cena' is missing"}), 400
    else:
        selected_pizza = None
        for pizza in nabidka:
            if pizza["název"] == nazev:
                pizza["cena"] = cena
                selected_pizza = pizza
                break
        if not selected_pizza:
            return jsonify({"error": "jmeno not found"}), 400
        else:
            nabidka.remove(selected_pizza)
            return jsonify(selected_pizza), 200

@app.route("/api/pica", methods=["DELETE"])
def api_delete_picy():
    nazev = request.args.get("jmeno")
    if not nazev:
        return jsonify({"error": "Parameter 'jmeno' is missing"}), 400
    else:
        selected_pizza = None
        for pizza in nabidka:
            if pizza["název"] == nazev:
                selected_pizza = pizza
                break
        if not selected_pizza:
            return jsonify({"error": "jmeno not found"}), 400
        else:
            nabidka.remove(selected_pizza)
            return jsonify({"success": f"Pizza '{nazev}' is deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    