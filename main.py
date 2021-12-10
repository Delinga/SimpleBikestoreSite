import mysql.connector
from flask import Flask, render_template, request

#______Connecting_to_Database__________bla

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

@app.route("/" , methods=['GET'])
def index():
    mycursor.execute("SELECT * FROM bikes")
    
    return render_template('index.html', bike_infos=mycursor)



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
