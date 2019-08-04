import tkinter as tk 
import requests

HEIGHT = 500
WIDTH = 600

def get_city(city):
  print(city)




def get_weather_data(city):
  key = 'openweathermap api key goes here'
  url = 'https://api.openweathermap.org/data/2.5/weather'
  params = {'APPID': key, 'q':city, 'units':'Celsius' }
  response = requests.get(url, params=params)
  weather_json = response.json()
  """
  {'coord': {'lon': -71.06, 'lat': 42.36}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'base': 'stations', 'main': {'temp': 295.5, 'pressure': 1013, 'humidity': 88, 'temp_min': 293.71, 'temp_max': 297.15}, 'wind': {'speed': 5.7, 'deg': 210}, 'clouds': {'all': 49}, 'dt': 1564894430, 'sys': {'type': 1, 'id': 4967, 'message': 0.0129, 'country': 'US', 'sunrise': 1564911573, 'sunset': 1564963265}, 'timezone': -14400, 'id': 4930956, 'name': 'Boston', 'cod': 200}

  """

  print(weather_json['name'])
  print(weather_json['sys']['country'])
  print(weather_json['weather'][0]['description'])
  print(weather_json['main']['temp'])

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_image = tk.PhotoImage(file='bg.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#00ace6', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

input = tk.Entry(frame, font=40)
input.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Test Button', font=40, command=lambda: get_weather_data(input.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

result_frame = tk.Frame(root, bg='#00ace6', bd=10)
result_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(result_frame, text='Weather App')
label.place(relwidth=1, relheight=1)

root.mainloop()
