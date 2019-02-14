from flask import Flask,render_template,request
import requests

app=Flask(__name__)
api_key="38c06d0f775ea03cb0d5cb8965d936b3"
url="http://data.fixer.io/api/latest?access_key="+api_key

@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST":
        firstCurrency=request.form.get("firstCurrency")
        secondCurrency=request.form.get("secondCurrency")
        amount=request.form.get("amount")
        response=requests.get(url) #sayfadan dövizleri çekiyor
        infos=response.json()
        firstValue=infos["rates"][firstCurrency]
        secondValue=infos["rates"][secondCurrency]
        result=(secondValue/firstValue)*float(amount)
        currencyInfos=dict()
        currencyInfos["firstCurrency"]=firstCurrency
        currencyInfos["secondCurrency"]=secondCurrency
        currencyInfos["amount"]=amount
        currencyInfos["result"]=result
        return render_template("index.html",info=currencyInfos)
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)