import mysql.connector
from flask import Flask, render_template

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

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)