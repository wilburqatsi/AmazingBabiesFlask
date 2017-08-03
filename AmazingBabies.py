from flask import Flask, render_template
import CatFacts
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

cat = CatFacts.CatFacts()

@app.route('/')
def index():

    cat.setRandomCat()
    name = cat.getCatName()
    fact = cat.getCatFact()
    pic = cat.getCatPic()
    species = cat.getSpecies()

    return render_template("index.html", name = name, fact = fact, pic = pic, species = species)


if __name__ == '__main__':
    app.run()
