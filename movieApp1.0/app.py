from flask import Flask, render_template, render_template_string
import os
from movieScraper import Scraper

# sc = Scraper(["rank", "movie", "status"])
sc = Scraper()

app = Flask(__name__)

@app.route("/")
def index():
    # return '<h2>The List Of 100 Greatest Movies Of All Time</h2><a href="/new">Generate New List</a>'
    # return render_template_string(os.path.dirname(__file__) + "/src/index.html")
    # return render_template_string('src/index.html')
    return render_template('index.html')


@app.route("/new/")
def newList():
    sc.generateMovieList(Scraper.fieldnames)
    Scraper.tempDB = sc.readFile(Scraper.fieldnames)
    statusStyle = "style=\"color:darkred\""
    html = "<p><a href=\"/\">Back</a></p><ul>"
    for i in Scraper.tempDB:
        statusStyle = "style=\"color:darkgreen\"" if (i['status'] == "seen") else "style=\"color:darkred\""
        html += (f"<li>{i['rank']} {i['movie']} <span {statusStyle}>{i['status']}</span> <button onclick=\"window.location.href='/mark/{i['movie']}';\">seen</button></li>")
    html += ("</ul>")
    return html

@app.route("/list/")
def getList():
    Scraper.tempDB = sc.readFile(Scraper.fieldnames)
    statusStyle = "style=\"color:darkred\""
    html = "<p><a href=\"/\">Back</a></p><ul>"
    for i in Scraper.tempDB:
        statusStyle = "style=\"color:darkgreen\"" if (i['status'] == "seen") else "style=\"color:darkred\""
        html += (f"<li>{i['rank']} {i['movie']} <span {statusStyle}>{i['status']}</span> <button onclick=\"window.location.href='/mark/{i['movie']}';\">seen</button></li>")
    html += ("</ul>")
    return html

@app.route("/get/")
def getMovie():
    Scraper.tempDB = sc.readFile(Scraper.fieldnames)
    if not sc.checkMovieStatus(Scraper.tempDB):
        return "<p><a href=\"/\">Back</a></p><h3>There is nothing else to watch</h3><h4>Cheers!</h4>"
    movie = sc.getRandomMovie(Scraper.tempDB)
    sc.writeFile(Scraper.tempDB, Scraper.fieldnames)
    return f"<p><a href=\"/\">Back</a></p><h3>{movie}</h3>"

@app.route("/add/")
def add():
    return "<input id=\"movie\" type=\"text\"></input>\
    <button onclick=\"addMovie()\">Add</button>\
    <script>function addMovie(){window.location.href+=document.querySelector('#movie').value}</script>"

@app.route("/add/<movie>")
def addMovie(movie):
    res = sc.addNewMovie(movie, Scraper.tempDB, Scraper.fieldnames)
    if res:
        return f"<p><a href=\"/\">Back</a></p><h3>'{movie}' added to the list</h3>"
    return f"<p><a href=\"/\">Back</a></p><h3>'{movie}' is already in the list</h3>"

@app.route("/mark/")
def mark():
    return "<input id=\"movie\" type=\"text\"></input>\
    <button onclick=\"markMovie()\">Mark</button>\
    <script>function markMovie(){window.location.href+=document.querySelector('#movie').value}</script>"

@app.route("/mark/<movie>")
def markMovie(movie):
    res = sc.markMovieAsSeen(movie, Scraper.tempDB, Scraper.fieldnames)
    if res:
        return f"<p><a href=\"/\">Back</a></p><h3>'{movie}' status changed to 'seen'</h3>"
    return "<p><a href=\"/\">Back</a></p><h3>No such movie in the list</h3>"

# if __name__ == "__main__":
#     # port = int(os.environ.get("PORT", 5000))
#     # # app.run(debug=True, host="0.0.0.0", port=port)
#     # app.run(host="0.0.0.0", port=port)
#     app.run()


# python3 -m flask run