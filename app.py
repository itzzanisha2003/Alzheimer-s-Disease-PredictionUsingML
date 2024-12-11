from flask import render_template, request, url_for, redirect, flash, Flask
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/')
def init():
    return render_template("index.html")  


@app.route('/', methods=['GET', 'POST'])
def index():
    a = int(request.form.get("Visit"))
    b = int(request.form.get("M/R Delay"))
    c = int(request.form.get("M/F"))
    
    d = int(request.form.get("Age"))
    e = int(request.form.get("eDUC"))
    f =int(request.form.get("MMSE"))
    m =int(request.form.get("SES"))
    g = float(request.form.get("CDR"))
    h = int(request.form.get("eTIV"))
    i = float(request.form.get("nWBV"))
    j = float(request.form.get("ASF"))
    print (type(a))
    print (type(b))
    print (type(c))
    print (type(d))
    print (type(e))
    print (type(f))
    print (type(g))
    print (type(h))
    print (type(i))
    print (type(j))

    clf = joblib.load("alzheimer.pkl")
    x = pd.DataFrame([[a,b,c,d,e,f,m,g,h,i,j]], columns=['Visit', 'M/R Delay', 'M/F',
       'Age', 'eDUC', 'MMSE','SES','CDR', 'eTIV','nWBV','ASF'])
    prediction = clf.predict(x)[0]
    
    output=prediction

    if output == 1:
            return render_template('index.html', 
                               result = 'The patient is likely to have demented disease!')
    elif output==0:
        return render_template('index.html', 
                               result = 'The patient is  likely to have nondemented disease!')
    else:
         return render_template('index.html', 
                               result = 'The patient is  likely to have converted disease!')
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)