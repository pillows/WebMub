from flask import url_for, Blueprint, render_template, redirect, session, flash, request
from config import *
import urllib2
import os
index=Blueprint("index",__name__)

@index.route("/",methods=['GET','POST'])
def index_():
    webm = db.webm.find().sort("points",-1)
    return render_template("index.html",webm=webm)