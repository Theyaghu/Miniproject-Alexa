import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests, json



listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('I am your alexa')
engine.say('what can i do for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice =listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command= command.replace('alexa' , '')

    except:
        pass

    return command

def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play' , '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Curent time is ' + time)
    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'weather' in command:
        api_key = "Your_API_Key"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = input("Enter city name: ")
        talk("Enter city name")
        complete_url = base_url + "appide=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x['cod'] != '404':
            y = x['main']
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            report = "Temperature (in kelvin unit) = " + str(current_temperature) + "\n Atmospheric Pressure = " + str(
                current_pressure) + "\n Humidity =" + str(current_humidity) + "\n Description = " + str(
                weather_description)
            # print("Temperature (in kelvin unit) = " + str(current_temperature)+"\n Atmospheric Pressure = " + str(current_pressure) +"\n Humidity =" + str(current_humidity)+ "\n Description = " + str(weather_description))
            print(report)
            talk(report)
        else:
            print("City Not Found")


    else:
        talk('Please say the command again.')
while True:
   run_alexa()
