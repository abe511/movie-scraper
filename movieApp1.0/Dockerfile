# setup
FROM        python:3.11-rc-alpine3.15
WORKDIR     /usr/src/app

# install dependencies
COPY        requirements.txt ./
RUN         pip install -r requirements.txt

# set env vars
ENV         FLASK_APP=app.py
ENV         FLASK_RUN_HOST=0.0.0.0

# copy files
COPY        ./templates/ ./templates/
COPY        movieScraper.py .
COPY        app.py .

EXPOSE 5000


# run the app

# working
# CMD         python3 app.py

CMD         ["flask", "run"]


# docker build -t app --rm .
# docker run -it --rm app