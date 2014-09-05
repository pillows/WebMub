from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
index=Blueprint("index",__name__)

@index.route("/",methods=['GET','POST'])
def index_():
    return render_template("index.html")