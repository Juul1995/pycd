from flask import Flask
import random

app = Flask(__name__)

# Print a random number between 0 and 10, I need to make it a string so Flask can print it. 
@app.route("/")
def number():
    return str(random.randint(0, 10))

print("And now you see this random number")


if __name__ == "__main__":
    app.run()

# virtual environment : $ source pipeline/Scripts/activate, $ deactivate 
#FLASK_APP=application:app flask run

#gunicorn is niet compatible met Windows! Inloggen op Linux eerst. 