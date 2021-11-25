from flask import render_template, request, redirect, Response
from fcr import  gen_frame
import mysql_connector as sq

# view template
def base():
    return render_template('base.html')

# home page
def index():
    return render_template('index.html')

def html_page(page_name):
    return render_template(page_name)

# presence system page
def presence():
    """Video streaming home page."""
    return render_template('presence.html')

def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def history():
    return sq.showRows()


    