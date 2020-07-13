import speech_recognition as sr

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I didn't get that !")
        except sr.RequestError:
            print("Sorry, my speech service is down !")

        return voice_data


print("How can I Help you ?")
voice_data = record_audio()
print(voice_data)
