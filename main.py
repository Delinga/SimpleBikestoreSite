import mysql.connector
from flask import Flask, render_template, request

#______Connecting_to_Database__________

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bikeshop"
)
mycursor = db.cursor()
#db.commit()
#______Connecting_to_Database_End__________

app = Flask(__name__)

@app.route("/" , methods=['GET','POST'])
def index():


    sort_brand = ''
    available_brands = []


    mycursor.execute("SELECT DISTINCT brand FROM bikes")
    for entry in mycursor:
        available_brands.append(entry[0])

    
    if request.method == "POST":
        sort_brand = request.form['brand']
        mycursor.execute("SELECT * FROM bikes WHERE brand = %s", (sort_brand,))
        print(sort_brand)
        return render_template('index.html', brands=available_brands, bike_infos=mycursor)

    mycursor.execute("SELECT * FROM bikes")

    return render_template('index.html', brands=available_brands, bike_infos=mycursor)



@app.route("/admin" , methods=['POST', 'GET'])
def admin():

    if request.method == "POST":
        try:
            mycursor.execute("INSERT INTO bikes (brand, model, year, picture) VALUES (%s,%s,%s,%s)", (request.form['brand'], request.form['model'], request.form['year'], "stoic2_2021.webp"))
            db.commit()
            return render_template("admin.html")
        except:
            return "Ein Fehler ist aufgetreten"
    else:
        return render_template("admin.html")
    


if __name__ == "__main__":
    app.run(debug=True)
