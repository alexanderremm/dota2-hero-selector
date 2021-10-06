from flask import Flask
from flask import render_template
from flask import request

def convertHeroNameToURL(heroName):
    return heroName.replace(" ", "_")

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the hero name from the form
        hero = request.form['hero']
        # Convert the hero name to the url endpoint we are expecting
        heroURL = "https://dota2.fandom.com/wiki/" + convertHeroNameToURL(hero) + "/Counters"
        return render_template("index.html", new_url=heroURL)
    else:
        return render_template("index.html", new_url=None)

# Debug Driver script
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)