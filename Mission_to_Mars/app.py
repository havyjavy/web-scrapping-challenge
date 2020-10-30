from flask import Flask, render_template
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create variable for our connection string
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Connect to a database. 
# If the database doesn't already exist, our code will 
# create it automatically as soon as we insert a record.
db = client.mars_db

# Define index/home route
@app.route('/')
def index():
    results = mongo.db.collections.find_one()
    return render_template('index.htm', data_dict = results)

@app.route("/scrape") 
def scrape():

    data_dict = mission_to_mars.scrape()
    return render_template("index.html", listing_results=listing_results)


if __name__ == "__main__":
    app.run(debug=True)

