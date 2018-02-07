from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/ninja/<color>')
def ninjas(color):
  	return render_template("results.html", color=color)



app.run(debug=True) # run our server