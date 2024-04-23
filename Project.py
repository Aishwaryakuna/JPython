import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification
def getNotification():
    cityName=place.get()
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    try:
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(url)
        x = response.json()
        y = x["main"]
        temp = y["temp"]
        temp-=273
        pres = y["pressure"]
        hum = y["humidity"]
        z = x["weather"]
        weather_desc = z[0]["description"]
        info="Here is the eather description of "+ cityName+ ":"+" \nTemperature = " +str(temp) +"°C"+"\n atmospheric pressure = " + str(pres) + "hPa"+"\n humidity = " +str(hum) +"%"+"\n description of the weather= " + str(weather_desc)
        notification.notify(title = "YOUR WEATHER REPORT",message=info ,timeout=2)
        time.sleep(7)
    except Exception as e:
        mb.showerror('Error',e)
wn = Tk()
wn.title("PythonGeeks Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')
Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19',bg='azure').place(x=100,y=15)
Label(wn, text='Enter the Location:', font=("Courier", 13),bg='azure').place(relx=0.05, rely=0.3)
place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)
btn = Button(wn, text='Get Notification', font=7, fg='grey19',command=getNotification).place(relx=0.4, rely=0.75)
wn.mainloop()