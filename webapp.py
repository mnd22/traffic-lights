#! /usr/bin/env python3

from flask import Flask, render_template
import trafficlights as tl

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/trafficlightsapi/<colour>')
def trafficlightsapi(colour):
  if (colour == "red"):
    tl.redonly()
  elif (colour == "amber"):
    tl.amberonly()
  elif (colour == "green"):
    tl.greenonly()
  elif (colour == "redamber"):
    tl.redamber()
  elif (colour == "off"):
    tl.alloff()  
  elif (colour == "cycle"):
    tl.cyclelights()  
  else:
    colour = "Input not understood"
      
  return render_template('trafficlightsbasic.html', 
                          currentcolour = colour)

@app.route('/trafficlights')
def trafficlights():
  return render_template('trafficlights.html')

@app.route('/dicegame')
def dicegame():
  return render_template('dicegame.html')
  
if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')
