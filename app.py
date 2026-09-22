from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "umamusume.db"

def create_connection(db_file):
   try:
       connection = sqlite3.connect(db_file)
       return connection
   except Error as e:
       print(e)
   return None

@app.route('/')
def render_home():
   return render_template("index.html")

@app.route('/characters')
def render_cards():
    query = " FROM "
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query)
    card_list = cur.fetchall()
    con.close()
    return render_template("cards.html",cards=character_list)

@app.route('/horses')
def render_cards():
    query = " FROM "
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query)
    card_list = cur.fetchall()
    con.close()
    return render_template("horses.html",cards=horse_list)
