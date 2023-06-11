from flask import Flask, render_template, request, flash, redirect, url_for, session

from forms import *
import uuid


app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = uuid.uuid4().hex


urun = {"img": "https://lelolobi.com/wp-content/uploads/2021/11/Test-Logo-Small-Black-transparent-1-1.png",
        "name": "test", "desc": "asddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"}

slides = [
    ["Kişisel Bakım", "https://www.turuncukasa.com/blog/wp-content/uploads/2015/02/s-f760dacb865e1eae9e868a6a48c74d17a654af31.jpg"],
    ["Bilgisayar", "https://cdn.webtekno.com/media/cache/content_detail_v2/article/116260/turkiye-de-en-cok-kullanilan-teknolojik-urunler-belli-oldu-hani-televizyonlar-bitiyordu-1634560545.jpg"],
    ["Ofis", "https://www.ofmark.com/blog/wp-content/uploads/2020/12/Her-Ofiste-Bulunmas%C4%B1-Gereken-Ofis-Malzemeleri-1170x781.jpg"],
    ["Telefon", "https://img.tamindir.com/resize/1200x675/2023/02/470608/galaxy-s23-ozellikleri-fiyati-1.jpg"],

]


@app.route("/")
def main_page():

    return render_template("home_page.html", slides=slides, urunler=[urun, urun, urun, urun, urun, urun, urun, urun, urun, urun])


@app.route("/<category>", methods=['GET', 'POST'])
def category_page(category):

    #products = get_urun()

    return render_template("categories.html", category_name=category, urunler=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


@app.route("/<category>/<product_id>")
def product_page(category, product_id):

    #products = get_urun(product_id)
    product = 1
    return render_template("product_page.html", category_name=category, product=urun)


@app.route("/boxes")
def boxes_page():

    return render_template("boxes.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    kayit_form = KayitForm(request.form)
    giris_form = GirisForm(request.form)

    if request.method == 'POST' and giris_form.validate():

        # get_user_info
        session["username"] = "giris_form.name.data "

        flash('Başarıyla giriş yapıldı...')
        return redirect(url_for('login'))
    if request.method == 'POST' and kayit_form.validate():

        # db_session.add(user)

        session["username"] = kayit_form.name.data

        flash('Başarıyla kayıt olundu...')
        return redirect(url_for('login'))
    session["isLoggedIn"] = False
    flash('Bilgilerde hata yapıldı...')
    return render_template('register.html', kayit_form=kayit_form, giris_form=giris_form)


@app.route("/login", methods=["POST", "GET"])
def login():

    session["isLoggedIn"] = True
    return redirect("/")


@app.route("/logout")
def logout():
    session["isLoggedIn"] = False
    session["username"] = None
    flash("Çıkış yapılmıştır...")
    return redirect("/")


if __name__ == "__main__":

    app.run(debug=True)
