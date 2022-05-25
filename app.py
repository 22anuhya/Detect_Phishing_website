from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)


@app.route("/")
def test():
    return render_template("index.html")

@app.route("/predict", methods = ['POST'])
def index():
    if request.method == "POST":
        domain = str(request.form['domain'])
        rank=int(request.form['rank'])
        ip=int(request.form['isIp'])
        valid=int(request.form['valid'])
        activeDuration=int(request.form['activeDuration'])
        urllen=int(request.form['urllen'])
        isat=int(request.form['is@'])
        isredirect=int(request.form['isredirect'])
        haveDash=int(request.form['haveDash'])
        domainLen=int(request.form['domainLen'])
        noOfSubdomain=int(request.form['noOfSubdomain'])
        data=np.array([[domain,rank,ip,valid,activeDuration,urllen,isat,isredirect,haveDash,domainLen,noOfSubdomain]])

        model = "F:\Projects sem4\PhishingDetection\model.pkl"
        predictor = pickle.load(open(model, "rb"))
        my_prediction = int(predictor.predict(data))
        if my_prediction==1:
            res='It is not a Safe Website'
        else:
            res='It is a Safe Website'
    return render_template('result.html', result = res)
  
@app.route("/so")
def so():
    data = np.array([['fvyhjy',1,2,3,4,0,0,1,20,0,2]])
    predictor = pickle.load(open('model.pkl', 'rb'))
    my_prediction = int(predictor.predict(data))

    print(my_prediction)

app.run()