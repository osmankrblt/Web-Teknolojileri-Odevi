from flask import Flask, render_template, request, flash, redirect, url_for, session
from db_services import *
import random
from forms import *
import uuid


app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = uuid.uuid4().hex


slides = [
    ["Kişisel Bakim", "https://www.turuncukasa.com/blog/wp-content/uploads/2015/02/s-f760dacb865e1eae9e868a6a48c74d17a654af31.jpg"],
    ["Bilgisayar", "https://cdn.webtekno.com/media/cache/content_detail_v2/article/116260/turkiye-de-en-cok-kullanilan-teknolojik-urunler-belli-oldu-hani-televizyonlar-bitiyordu-1634560545.jpg"],
    ["Ofis", "https://www.ofmark.com/blog/wp-content/uploads/2020/12/Her-Ofiste-Bulunmas%C4%B1-Gereken-Ofis-Malzemeleri-1170x781.jpg"],
    ["Telefon", "https://img.tamindir.com/resize/1200x675/2023/02/470608/galaxy-s23-ozellikleri-fiyati-1.jpg"],

]


products = sync()


@app.route("/")
def main_page():

    return render_template("home_page.html", slides=slides, urunler=random.sample(products, 20))


@app.route("/<category>", methods=['GET', 'POST'])
def category_page(category):

    return render_template("categories.html", category_name=category, urunler=getProductsByCategory(category, products))


@app.route("/<category>/<product_id>")
def product_page(category, product_id):

    return render_template("product_page.html", category_name=category, urun=products[int(product_id)])


@app.route("/boxes")
def boxes_page():

    return render_template("boxes.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    kayit_form = KayitForm(request.form)
    giris_form = GirisForm(request.form)

    if request.method == 'POST' and kayit_form.validate():

        addUser(kayit_form)

        session["username"] = kayit_form.name.data

        flash('Başarıyla kayıt olundu...')
        return redirect(url_for('login'))

    if request.method == 'POST' and giris_form.validate():

        if checkUser(giris_form) == True:

            flash('Başarıyla giriş yapıldı...')
            return redirect(url_for('login'))
        else:
            flash('Böyle bir kullanıcı bulunamadı veya hatalı bilgi girildi...')
            return render_template('register.html', kayit_form=kayit_form, giris_form=giris_form)

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
