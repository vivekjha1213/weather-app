from flask import Flask,render_template,request
import requests,time



app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():
     if request.method == "POST":
            city = request.form['city'] 
            #api used from open source weather.
            api = "https://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=0eee0acfc032ab0d4028233b6cb4b7f3"
            response = requests.get(api)
            data = response.json()
            temp = round(data['main']['temp'] - 273.15)
            pressure = data['main']['pressure']
            humidity= data['main']['humidity']
            sunrise = time.strftime('%I:%M',time.gmtime(data['sys']['sunrise'] -21600))
            sunset = time.strftime('%I:%M',time.gmtime(data['sys']['sunset'] -21600))
        
            return render_template('index.html',city=city,temp=temp,pressure=pressure,humidity=humidity,sunrise=sunrise,sunset=sunset)
     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    