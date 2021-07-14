import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib #for emails
import webbrowser
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)


def speak(message):
    engine.say(message)
    engine.runAndWait()


def time():
    speak('The current time is:')
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month =int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('The current date is :')
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir!!")

    hour=datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak("Good afternoon")
    elif 18 <= hour <= 24:    #chained version hour<=18 and hour<=24
        speak('Good evening')
    else:
        speak('Good night')


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.........')
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        print('Recognizing......')
        query=r.recognize_google(audio)

    except Exception as e:
        print(e)
        speak('Say that again please....')
        return 'None'
    return query


def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourmail','password')
    server.sendmail('receiver mail id',to,content)
    server.close()


def screenshot():
    img=pyautogui.screenshot()
    img.save('screenshot.png')

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery=psutil.sensors_battery()
    speak('battery is at:')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__=="__main__":
    wishme()
    speak('How can I help you ?')
    while True:
        query=takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("See you later.......")
            quit()
        elif "wikipedia" in query:
            speak('searching........')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "send email" in query:
            try:
                speak('What should I say?')
                content=takeCommand()
                to='receiver mail id'
                sendmail(to,content)
                speak('The mail was sent successfully')
            except Exception as e:
                speak(e)
                speak('Unable to send the email')
        elif "search in chrome" in query:
            speak("What should I search?")
            search=takeCommand().lower()
            webbrowser.open_new_tab(search+".com")

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_dir="H:\songs"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "remember" in query:
            speak('What should I remember')
            data=takeCommand()
            speak('you said me to remember'+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak('you said me to remeber that'+remember.read())

        elif 'screenshot' in query:
            screenshot()

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()
        






