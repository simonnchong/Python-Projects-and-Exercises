from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return \
    "<h1 style='text-align: center'>Hello World</h1>" \
    "<p>This is a paragraph</p1>" \
    "<img src='https://cloudinary-assets.dostuffmedia.com/res/dostuff-media/image/upload/page-image-3732-952a384e-e157-4a5f-9369-bb3c645aad62/1440186818.gif' width=100%>"

@app.route("/say_bye")
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old."

if __name__ == "__main__":
    app.run(debug=True)