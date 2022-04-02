from flask import Flask, render_template, request, redirect, url_for

from equipment import Equipment

app = Flask(__name__)




@app.route("/")
def mane_page():
    return render_template("index.html")


@app.route("/choose-hero/", methods=['GET', 'POST'])
def choose_hero():
    if request.method == "GET":
        header = "Выберите героя"
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        classes = unit_classes
        return render_template(
            "hero_choosing.html",
            result={
                "header": header,
                "classes": classes,
                "weapons": weapons,
                "armors": armors
            }
        )
    if request.method == "POST":
        name = request.form["name"]
        armor_name = request.form["armor"]
        weapon_name = request.form["weapon"]
        unit_class = request.form["unit_class"]
        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class))
        player.equip_weapon(Equipment().get_weapon(weapon_name))
        player.equip_armor(Equipment().get_armor(armor_name))
        heroes["player"] = player
        return redirect(url_for("choose_enemy"))