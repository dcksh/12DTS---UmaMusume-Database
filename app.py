from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "C:/Users/daksh/PycharmProjects/12DTS---UmaMusume-Database/identifier.sqlite"

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
def render_characters():
    query = "SELECT eng_name, rom_name, jap_name, star_rarity, voice_actor, height, measurements, character_weight, shoe_size, roommate, emoji, likes, dislikes, ears, tail, family, personal_rule, background, secrets, global_status, strategy_aptitude, distance_aptitude, surface_aptitude, unique_skill, alt_outfits FROM umamusume"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query)
    character_list = cur.fetchall()
    con.close()
    print(character_list)
    return render_template("characters.html",characters=character_list)

@app.route('/horses')
def render_horses():
    query = "SELECT sex, dam, sire, birth_year, horse_weight, country, jockey, owner, farm, record, total_earnings, notable_wins, offspring, deceased_status FROM umamusume"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query)
    horse_list = cur.fetchall()
    con.close()
    print(horse_list)
    return render_template("horses.html",horses=horse_list)
