from flask import Flask, render_template, json
import CatFacts
from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)

cat = CatFacts.CatFacts()

@app.route('/')
def index():

    cat.setRandomCat()
    name = cat.getCatName()
    fact = cat.getCatFact()
    picArray = []
    picArray.append(cat.getCatPic())

    species = cat.getSpecies()
    picArray.extend(cat.getThumbnails())


    return render_template("index.html", name = name, fact = fact, \
                           species = species, jsonPicArray = json.dumps(picArray), picArray = picArray)



if __name__ == '__main__':
    app.run()
