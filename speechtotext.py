#speech  to text

import speech_recognition as sr
print("welcome to conversion of audio to text")
sp=input("enter the audio source file in wav form:")
AUDIOFILE=(sp)
r=sr.Recognizer()#initializing the recognizer
with sr.AudioFile(AUDIOFILE) as source:
    audio=r.record(source)
try:
    print("audio file contains\n"+r.recognize_google(audio))
except sr.UnknowValueError:
    print("google speech recognition could not understand audio")
except sr.RequestEror:
    print("could not get the result from google speech Regonition")
