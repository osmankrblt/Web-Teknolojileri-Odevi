from flask import Flask, render_template,request,flash,redirect,url_for

from forms import RegisterForm

app = Flask(__name__, template_folder="templates")


@app.route("/")
def main_page():

    return render_template("home_page.html", images=[1, 2, 3, 4, 5], urunler=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


@app.route("/<category>", methods=['GET', 'POST'])
def category_page(category):

    #products = get_urun()

    return render_template("categories.html", category_name=category, urunler=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


@app.route("/<category>/<product_id>")
def product_page(category, product_id):

    #products = get_urun(product_id)
    product = 1
    return render_template("product_page.html", category_name=category, urun=product)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        print(form)
        #db_session.add(user)
        flash('Başarıyla kayıt olundu...')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == "__main__":

    app.run(debug=True)
