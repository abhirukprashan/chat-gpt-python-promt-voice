import speech_recognition as sr
import openai
import pyttsx3

engine = pyttsx3.init()

r= sr.Recognizer()

openai.api_key = "access token here"


while True:
    with sr.Microphone() as source:
      print('ask the question: ')
      audio = r.listen(source)

      try:
        text = r.recognize_google(audio)
        output = openai.ChatComletion.create(model = "gpt-3.5-turbo",message=[{"role":"user","content":text}]) 
        engine.say(output)
        engine.runAndWait()
        
      except:
        print("sorry speak again")