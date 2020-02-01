import os
from app import app
from flask import render_template, request, redirect
import csv
import json
import pandas as pd
import sys, getopt, pprint
import random
csvfile = open('/Users/2020jkapasi/Desktop/CompSci_IA/Book1.csv', "r")
reader = csv.DictReader(csvfile)

header = ["Category","Author","Title/Subtitle","Barcode","Circ Type","Description 1","Description 2","Description 3","ISBN","Subject"]










events = [
    ]
from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:tsul0w85xQtsdZJa@cluster0-3rv5u.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/input')
def input():
    return render_template('input.html')



# INDEX

@app.route('/')
@app.route('/index')

def index():
    #connects the events to the mongo database
    collection = mongo.db.book
    books = list(collection.find({}))
    unique_category = []
    for x in books:
        if x["Category"] not in unique_category:
            unique_category.append(x["Category"])
    print(unique_category)
    print(books[0])
    return render_template("input.html")




@app.route('/results', methods = ["Get", "Post"]) #initiating the route
def results(): #defining the results page
    userdata = dict(request.form) #the user data is a dictionary of the form we created (inputs)
    print(userdata) # test to see in terminal
    radiobutton = userdata["genre"]



    collection = mongo.db.book #connecting to the Mongo database (the events collection within the databse)

    #find the events in the collection, store them as a list of dictionaries, and assign to X.
    x = list(collection.find({"Category":radiobutton})) #

    y = (random.sample(x, k=3))
    return render_template("specific.html", y=y)
