from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re




class CatFacts:


    def __init__(self):
        felidae_html = urlopen("http://en.wikipedia.org/wiki/Felidae")
        felidae_bsObj = BeautifulSoup(felidae_html, "html.parser")

        #initialize list that contains cat species URLs
        self.catUrl = []

        # Grabs second table on wiki page
        catList = felidae_bsObj.findAll("table")[2] \
            .findAll("a", {"class": "mw-redirect", "href": re.compile("^(/wiki/)((?!:).)*$")})
        for link in catList:
            self.catUrl.append(link.attrs["href"])

        #choose random cat page
        try:
            currentCat = self.catUrl[random.randint(0, len(self.catUrl) - 1)]

        except:
            print("catURL list may be empty")

        currentHTML = urlopen("http://en.wikipedia.org" + currentCat)

        self.currentPage = BeautifulSoup(currentHTML, "html.parser")


    def getCatName(self):
        return self.currentPage.find("h1").get_text()



    def getCatFact(self):

        # list of a <p> elements on page
        catFactList = self.currentPage.find("div", {"class": "mw-parser-output"}).findAll("p", recursive=False)

        return re.sub(r'\[.+?\]', '', catFactList[random.randint(0, len(catFactList) - 1)].get_text())


    def getCatPic(self):
        catPicLink = self.currentPage.find("a", {"class": "image"}).attrs["href"]
        catImageHtml = urlopen("http://en.wikipedia.org" + catPicLink)
        catImageObj = BeautifulSoup(catImageHtml, "html.parser")

        return "https:" + catImageObj.find("a", {"class": "internal"}).attrs["href"]

    def setRandomCat(self):
        newCat = self.catUrl[random.randint(0, len(self.catUrl) - 1)]
        newHTML = urlopen("http://en.wikipedia.org" + newCat)
        self.currentPage = BeautifulSoup(newHTML, "html.parser")

    def getSpecies(self):
        catSpecies = self.currentPage.find("span", {"class":"binomial"}).get_text()
        return re.sub(r'\[.+?\]', '', catSpecies)
