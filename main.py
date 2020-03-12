from tkinter import *
import requests


def format_response(weather):
    try:
        name=(weather['name'])
        desc=(weather['weather'][0]['description'])
        temp=(weather['main']['temp'])

        final= 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final= 'No information found'

    return final    

def get_weather(city):
    weather_key='6a9916dd197db8ba159c41cfd8214275'
    url ='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params=params)
    weather=response.json()

    label['text'] = format_response(weather)

    



root = Tk()

canvas = Canvas(root,width=600,height = 500)
canvas.pack()

background_img=PhotoImage(file='abc.png')
background_label=Label(root,image=background_img)
background_label.place(relwidth=1,relheight=1)


frame = Frame(root,bg="black",bd=5)
frame.place(relx=0.5,rely=0.1, relwidth=0.75,relheight=0.1,anchor=N)

entry=Entry(frame,font=20)
entry.place(relx=0,rely=0,relwidth=0.65,relheight=1)

button = Button(frame,text="Get Weather", font=20,command= lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0,relwidth=0.3,relheight=1)



lowerframe=Frame(root,bg="black",bd=5)
lowerframe.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor=N)

label = Label(lowerframe,font = 50)
label.place(relx=0,rely=0,relwidth=1,relheight=1)
root.mainloop()



