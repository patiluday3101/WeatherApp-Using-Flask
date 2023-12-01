from flask import Flask , render_template, request
import requests 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index11.html")
@app.route('/weatherapp',methods=["POST","GET"])
def get_weatherdata():
    url="https://api.openweathermap.org/data/2.5/weather"
    key="3bbcc3a8d2b8974a999e27a322c1669d"
    params = {'q' :request.form.get("city"),
        #   'appid' :request.form.get("appid"),
            'appid' :key,
          'units':request.form.get("units")}

    responce=requests.get(url,params=params) 
    data=responce.json() 
    return f"data : {data}"


if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5001)

