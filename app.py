from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    url_length = int(request.form["url_length"])
    dots = int(request.form["dots"])
    https = int(request.form["https"])
    special_char = int(request.form["special_char"])
    subdomain = int(request.form["subdomain"])

    features = np.array([[url_length,dots,https,special_char,subdomain]])

    prediction = model.predict(features)

    if prediction == 1:
        result = "Phishing URL"
    else:
        result = "Legitimate URL"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)