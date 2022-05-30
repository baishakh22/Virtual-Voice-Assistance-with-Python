import speech_recognition as sr        #it will recognize my voice
import pyttsx3                          #text to speech
import datetime                         #python built-in
import pywhatkit                        #additional setup like youtube, whatsapp
import wikipedia
import pyjokes                          #built-in jokes package
import python_weather                   #weather package
import asyncio                          #python framework


listener = sr.Recognizer()
maya = pyttsx3.init()                   #maya work for text to speech
voices = maya.getProperty('voices')     # it give me all voice property
maya.setProperty('voice', voices[1].id) #I use second element's ID.



#text paremeter give different situation
def talk(text):
    maya.say(text)
    maya.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:             #it call my laptop's microphone
                    print('Listening...')                   #test my microphone is ready or not
                    voice = listener.listen(source)         #it listen my voice
                    command = listener.recognize_google(voice)      #this is google API, I send voice to goggle and it will capture as text
                    command = command.lower()               #all text will be lower case
                    if 'maya' in command:                   #only maya can reponse, other command will not be recongnize
                        command = command.replace('maya', '') #maya will replace the word whatever I will say
    except:
        pass
    return command


def run_maya():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Right now is ' + time)

    elif 'today' in command:
        day = datetime.datetime.now().strftime("%A %d. %B %Y")
        print(day)
        talk('today is ' + day)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        wiki_search = command.replace('tell me about', '')
        info = wikipedia.summary(wiki_search, 2)
        print(info)
        talk(info)

    elif 'jokes' in command:
        talk(pyjokes.get_joke())

    elif 'date' in command:
        talk('We can date, but you must be romantic')

    elif 'weather' in command:

        async def getweather():
            client = python_weather.Client(format=python_weather.IMPERIAL)
            weather = await client.find('New York City')
            print(weather.current.temperature)
            talk(weather.current.temperature)
            await client.close()

        if __name__ == "__main__":
            loop = asyncio.get_event_loop()

            loop.run_until_complete(getweather())

    elif 'math' in command:
        talk('I am so dumb to do math')

    elif 'marry' in command:
        talk('How much money do you make?')

    elif 'about me' in command:
        talk('You are Muhfat Alam. Live in Bronx, New York. You are a undergraduate student in John Jay college.')
        talk('You major is computer science and information Security. And you are married with Vabna in june 25 2021')

    elif 'movie star' in command:
        talk('Tom Hanks')

    elif 'send message to' in command:
        wife = command.replace('send message to', '')
        talk('sending message to ' + wife)
        pywhatkit.sendwhatmsg('+8801675576901', 'Hi, what is up', 13, 46, True, 2)

    elif 'set up an alarm' in command:
        wake_up = command.replace('set up an alarm', '')
        talk('setting up the alarm')
        alarm_hour = 15
        alarm_minute = 27
        while True:
            if(alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute):
                talk("wake up you lazy.........")
                break


    else:
        talk('I am unable to get this, but i am opening a google search page for you')
        pywhatkit.search(command)

while True:
    run_maya()