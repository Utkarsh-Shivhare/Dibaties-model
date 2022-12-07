from pyexpat import features
from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template(index.html)

@app.route('/predict',methods=["POST","GET"])
def predict():
    features=[int(x) for x in request.form.values()]
    prediction=model.predict_proba(final)
    output='{0:{1}f}'.format(prediction[0][1],2)

    if output>str(0.5):
        return render_template('index.html',pred='You have dibaties. \nprobability of having dibaties is {}'.format(output))
    else:
        return render_template("index.html",pred="You are safe \nprobability of having dibatiews is {}".format(output))
if __name__=="__main__":
    app.run()