from flask import Flask, render_template
import CatFacts
from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)

cat = CatFacts.CatFacts()

@app.route('/', methods=['GET', 'POST'])
def index():

    cat.setRandomCat()
    name = cat.getCatName()
    fact = cat.getCatFact()
    print(name)
    pic = cat.getCatPic()
    #print(pic)
    species = cat.getSpecies()


    return render_template("index.html", name = name, fact = fact, pic = pic, species = species)



if __name__ == '__main__':
    app.run()
