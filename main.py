import speech_recognition as sr
import webbrowser
import time

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I didn't get that !")
        except sr.RequestError:
            print("Sorry, my speech service is down !")

        return voice_data


def response(voice):
    if 'what is your name' in voice:
        print("I'm Batman !")
    if 'what time is it' in voice:
        print(time.asctime(time.localtime(time.time())))
    if 'search' in voice:
        search = record_audio('What do you wanna search for ?')
        url = 'https://google.com/search?q=' + search
        webbrowser.open(url)
        print('Here is what I found for ' + search)
    if 'location' in voice:
        location = record_audio('Where do you wanna go ?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.open(url)
        print('Here is what I found for ' + location)
    if 'exit' in voice:
        exit()


time.sleep(1)
print("How can I Help you ?")
while 1:
    voice_data = record_audio()
    response(voice_data)
