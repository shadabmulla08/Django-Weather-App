from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST.get('city','True')
        try:
            source=urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=99ed8109be9313a5cd83c79def0f7be2&units=metric").read()
            list_of_data=json.loads(source)
            context={
            'city': str(list_of_data['name']),  
            "country_code": str(list_of_data['sys']['country']),  
             "temp": str(list_of_data['main']['temp']) + 'C',  
            "pressure": str(list_of_data['main']['pressure']),  
            "humidity": str(list_of_data['main']['humidity']),  

        }
        except:
             context={
            'city': 'null',  
            "country_code": 'null',  
             "temp": 'null',  
            "pressure": 'null',  
            "humidity": 'null',  
        }
    else:
        context={}
    return render(request,'index.html',context)