from flask import Flask, render_template
#import pymongo
from flask_pymongo import PyMongo
import scrape_mars
from pprint import pprint

# Create an instance of our Flask app.
app = Flask(__name__)

# Create variable for our connection string
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
#client = pymongo.MongoClient(conn)
mongo = PyMongo(app)

# Connect to a database.
# If the database doesn't already exist, our code will
# create it automatically as soon as we insert a record.
#db = client.mars_db
#collections = db.mars_data

# Define index/home route


@app.route('/')
def index():
    results = mongo.db.mars_collections.find_one()
    return render_template('index.html', collections=results)
    # return "data script"


@app.route("/scrape")
def scrape():

    # data_dict = scrape_mars.scrape()
    # collections.insert_one(data_dict)
    # results = collections.find(data_dict)
    # for i in results:
    #     pprint(i)
    # return render_template("index.html", mars_data=data_dict)
    mars = mongo.db.mars_collections
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
