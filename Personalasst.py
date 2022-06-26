import speech_recognition as sr
import webbrowser
import datetime
import requests
import json

def weather():
 api_key = "5671c6607cd65545ea8c550d6b4d6af5"
 base_url = "https://api.openweathermap.org/data/2.5/weather?"
 city_name = audioinput()
 complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 response = requests.get(complete_url)
 x =response.json()
 if x["cod"] != "404":
    y = x['main']
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))
 else:
    print(" City Not Found ")

def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
    elif hour>12 and hour<18:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
    print("I am your Virtual Assistant Lavy. How Can I Help You?")


def audioinput():
    aud = sr.Recognizer()
    with sr.Microphone() as source:
      print('listening and processing')
      aud.pause_threshold = 0.7
      audio = aud.listen(source)
    try:
         print("understanding") 
         phrase = aud.recognize_google(audio, language='en-us')
         print("you said: ", phrase)

    except Exception as exp:
         print(exp)
         print("Can you please repeat that")
         return "None"
    return phrase

def theTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    print( "The time right now is " + hour + " Hours and " + min + " Minutes")


def theDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
    3: 'Wednesday', 4: 'Thursday',
    5: 'Friday', 6: 'Saturday',
    7: 'Sunday'}
    if day in Day_dict.keys():
     weekday = Day_dict[day]
     print(weekday)
     print("it's " + weekday)


if __name__ == '__main__':  
        greeting()
while (True):

        phrase = audioinput().lower()
        if "open google" in phrase:
         print("Opening Google ")
         webbrowser.open("www.google.com")
         continue
        if "open youtube" in phrase:
         print("Opening youtube ")
         webbrowser.open("www.youtube.com")
         continue
        elif "weather" in phrase:
         weather()
         continue
        elif "what day it is" in phrase:
         theDay()
         continue
        elif "what time it is" in phrase:
         theTime()
         continue 
        elif "bye" in phrase:
         print("Exiting...., Have a Good Day")
         exit()
        elif "open wikipedia" in phrase: 
         print("Opening wikipedia ")
         webbrowser.open("www.wikipedia.com")
         continue
        elif "what is your name" in phrase:
         print("I am lavy. your  virtual assistant")