import pyodbc
from flask import session


def sync():

    connection = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=Osman;DATABASE=web-teknolojileri;UID=sa;PWD=56895689;')
    cursor = connection.cursor()

    products = cursor.execute('SELECT * FROM dbo.products').fetchall()
    images = cursor.execute('SELECT * FROM dbo.image').fetchall()

    return list(map(list2urun, zip(products, images)))


def addUser(user):
    connection = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=Osman;DATABASE=web-teknolojileri;UID=sa;PWD=56895689;')
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO dbo.users  VALUES  (?,?,?,?,?)""", (user.name.data,
                   user.surname.data, user.email.data, user.password.data, user.address.data))

    cursor.commit()


def checkUser(user):
    connection = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=Osman;DATABASE=web-teknolojileri;UID=sa;PWD=56895689;')
    cursor = connection.cursor()
    cursor.execute(
        """SELECT * FROM dbo.users WHERE mail = '{}'  and password='{}' """.format(str(user.email.data).strip(), str(user.password.data).strip()))

    result = cursor.fetchall()
    if len(result) != 0:
        session["username"] = result[0][1]
        return True
    else:
        print("x")
        return False


def list2urun(x):
    categories = ["TELEFON",
                  "BILGiSAYAR",
                  "HOBi",
                  "EV",
                  "KişiSEL BAKiM",
                  "Ofis"
                  ]
    product, image = x[0], x[1]

    return {"id": product[0], "name": product[1], "desc": product[2], "cat": categories[product[3]-1], "img": str(image[2].decode('utf-8')), "price": product[5]}


def getProductsByCategory(category_name, products):

    temp = []
    for product in products:

        if product["cat"].lower() == category_name.lower():
            temp.append(product)

    return temp
