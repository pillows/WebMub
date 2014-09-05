from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
register=Blueprint("register",__name__)

@register.route("/register/",methods=['GET','POST'])
def register_():
    return render_template("register.html")