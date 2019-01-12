"""
Routes and views for the flask application.
"""
#Added comment for DEV001

#ADDED dev002

from datetime import datetime
from flask import render_template
from Neo4jApp import app
from objects import EntityModel

 

#Dev 
#added in dev004

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    org  = EntityModel("Organization")
    org.find("1")

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        rootName=org.get("name"),
        itemName="Organization",
        data=org.data,
        relations=org.relations
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/item/<itemName>/<itemID>')
def itemView(itemName, itemID):

    item  = EntityModel(itemName)
    item.find(itemID)
    
    return render_template(
        'item.html',
        title='Item',
        rootName=item.get("name"),
        itemName=itemName,
        itemID=itemID,
        data=item.data,
        relations=item.relations,
        year=datetime.now().year,
        message='Item: ' + itemName
    )

@app.route('/list/<parentName>/<parentID>/<itemName>')
def listView(parentName,parentID,itemName):

    parent  = EntityModel(parentName)
    parent.find(parentID)
    item  = EntityModel(itemName)    
    lst = parent.findRelated(itemName)

    return render_template(
        'list.html',
        title='List',
        year=datetime.now().year,
        message='List: ' + itemName,
        itemName=itemName,
        itemKey=item.keyField,
        header=item.data,
        data=lst
    )