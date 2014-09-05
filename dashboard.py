from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
dashboard=Blueprint("dashboard",__name__)

@dashboard.route("/dashboard/",methods=['GET','POST'])
def dashboard_():
    return render_template("dashboard.html")