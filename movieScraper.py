
import os
import requests
import csv
import random
from bs4 import BeautifulSoup


class Scraper:
    '''Description:
    Save page contents in a file
    Scan the page for tags containing movie names
    Extract and push the names to a list'''

    fieldnames = ["rank", "movie", "status"]
    tempDB = []
    
    def scraper(self, url):
        if not os.path.exists(os.path.dirname(__file__) + "/website.html"):
            pageContent = requests.get(url)
            with open(os.path.dirname(__file__) + "/website.html", "w") as htmlFile:
                htmlFile.write(pageContent.text)
        with open(os.path.dirname(__file__) + "/website.html", "r") as htmlFile:
            page = BeautifulSoup(htmlFile, "html.parser")
        titles = []
        movieHeaders = page.find_all("h3", attrs={"class":"title"})
        for h in movieHeaders:
            titles.append(h.string)
        return titles

    # get movie names and save them to csv file
    def generateMovieList(self, fieldnames):
        url = "https://web.archive.org/web/20200518073855/https:/www.empireonline.com/movies/features/best-movies-2/"
        movieDB = self.scraper(url)
        movieDB.reverse()
        fields = [{"rank": n, "movie":m.split(" ", 1)[1], "status": "not seen"} for n, m in enumerate(movieDB, start=1)]
        with open(os.path.dirname(__file__) + "/movies.csv", "w") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames)
            writer.writeheader()
            writer.writerows(fields)

    def readFile(self, fieldnames):
        if not os.path.exists(os.path.dirname(__file__) + "/movies.csv"):
            self.generateMovieList(fieldnames)
        with open(os.path.dirname(__file__) + "/movies.csv", "r") as csvFile:
            reader = csv.DictReader(csvFile, fieldnames)
            next(reader)
            tempDB = []
            for line in reader:
                tempDB.append(line)
        return tempDB

    def checkMovieStatus(self, tempDB):
        for entry in tempDB:
            if entry["status"] == "not seen":
                break
        else:
            return False
        return True

    def getRandomMovie(self, tempDB):
        found = False
        movie = ""
        while not found:
            movieNum = random.randint(1, 100)
            for entry in tempDB:
                if int(entry["rank"]) == movieNum:
                    if entry["status"] == "not seen":
                        found = True
                        movie = entry["movie"]
                        entry["status"] = "seen"
                    break
        return movie

    def writeFile(self, tempDB, fieldnames):
        with open(os.path.dirname(__file__) + "/movies.csv", "w+") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames)
            writer.writeheader()
            writer.writerows(tempDB)


    def addNewMovie(self, newMovie, tempDB, fieldnames):
        if tempDB == []:
            tempDB = self.readFile(fieldnames)
        for entry in tempDB:
            if entry["movie"] == newMovie:
                return False
        tempDB.append({"rank": int(tempDB[-1]["rank"]) + 1, "movie": newMovie, "status": "not seen"})
        self.writeFile(tempDB, fieldnames)
        return True

    def markMovieAsSeen(self, movieName, tempDB, fieldnames):
        if tempDB == []:
            tempDB = self.readFile(fieldnames)
        for entry in tempDB:
            if entry["movie"] == movieName:
                entry["status"] = "seen"
                break
        else:
            return False
        self.writeFile(tempDB, fieldnames)
        return True