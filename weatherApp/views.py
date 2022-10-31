from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.
def home(request):
    if request.method=="POST":
        API_KEY = 'c19ed1816474ca8bf30caf29f5821cbc'
        city = request.POST['city']
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        json = requests.get(api).json()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        content = {
            'name':json['name'],
            'weather':json['weather'][0]['main'],
            'weather_desc':json['weather'][0]['description'],
            'wind':float(json['wind']['speed'])*(18/5),
            'temp_k':json['main']['temp'],
            'temp_c':int(json['main']['temp']-273.15) ,
            'humidity':json['main']['humidity'],
            'time':current_time,
        }
    else:
        API_KEY = 'c19ed1816474ca8bf30caf29f5821cbc'
        city = 'Pune'
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        json = requests.get(api).json()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        content = {
            'name':json['name'],
            'weather':json['weather'][0]['main'],
            'weather_desc':json['weather'][0]['description'],
            'wind':float(json['wind']['speed'])*(18/5),
            'temp_k':json['main']['temp'],
            'temp_c':int(json['main']['temp']-273.15) ,
            'humidity':json['main']['humidity'],
            'time':current_time,
        }
    
    return render(request,'home.html',context=content)
