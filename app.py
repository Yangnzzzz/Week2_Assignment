from flask import Flask
from flask import render_template, request
#comment 2111112
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    return (render_template("index.html"))

if __name__ == "__main__":
    app.run()