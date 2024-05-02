import pyttsx3
import speech_recognition as sr
import webbrowser
import smtplib
import random
import wikipedia
import datetime
import os
import sys
import wolframalpha

# Initializing the Text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

# Function to speak
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

# Function to greet based on the time of the day
def greetMe():
    currentH = datetime.datetime.now().hour
    if 0 <= currentH < 12:
        speak('Good Morning!')
    elif 12 <= currentH < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant Jarvis!')
speak('How may I help you?')

# Function to recognize speech input
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query

# Main function
if __name__ == '__main__':
    # Initializing WolframAlpha Client
    app_id = "YOUR_WOLFRAMALPHA_APP_ID"
    client = wolframalpha.Client(app_id)

    while True:
        query = myCommand().lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open whatsapp' in query:
            speak('okay')
            webbrowser.open('https://web.whatsapp.com/')

        elif 'open my channel' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/channel/UCoxgTwtoEG9T91RShZDEmgw')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = 'Your_music_folder_path'
            music = ['music1', 'music2', 'music3', 'music4', 'music5']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')

        else:
            speak('Searching...')
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('WOLFRAM-ALPHA says - ')
                speak('Got it.')
                speak(results)
            except:
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
                except:
                    webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
