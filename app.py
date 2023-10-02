import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    age = request.form['Age']
    print(age)
    sex = request.form['Sex']
    if sex == 'Male':
        sex = 1
    if sex == 'Female':
        sex = 0
    bp = request.form['BP']
    if bp == 'Low':
        bp = 0
    if bp == 'Normal':
        bp = 1
    if bp == 'High':
        bp = 2
    chol = request.form['Cholesterol']
    if chol == 'Normal':
        chol = 0
    if chol == 'High':
        chol = 1
    na = float(request.form['Na_to_K'])
    t = [[int(age), int(sex), int(bp), int(chol), float(na)]]
    print(t)
    pred = model.predict(t)
    print(pred)
    return render_template("submit.html", prediction_text = "{}".format(pred))

if __name__ == "__main__":
    flask_app.run(debug=True)