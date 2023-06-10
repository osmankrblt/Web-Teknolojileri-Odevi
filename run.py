from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def main_page():

    return render_template("home_page.html", images=[1, 2, 3, 4, 5], urunler=[1, 2, 3, 4])


if __name__ == "__main__":

    app.run(debug=True)
