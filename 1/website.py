from flask import Flask, render_template
app = Flask(__name__)

@app.route('/roots/1/')
def rf():
   return render_template('regulafalsi.html')

@app.route('/roots/2/')
def nr():
   return render_template('newtonraphson.html')

@app.route('/roots/3/')
def itr():
   return render_template('iterative.html')

@app.route('/roots/4/')
def gse():
   return render_template('guasselimination.html')

@app.route('/roots/5/')
def gsjo():
   return render_template('guassjordan.html')

@app.route('/roots/6/')
def gsja():
   return render_template('guassjacobi.html')

@app.route('/roots/7/')
def gsse():
   return render_template('guassseidal.html')


if __name__ == '__main__':
   app.run(debug = True)