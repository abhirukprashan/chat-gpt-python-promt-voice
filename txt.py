import pyttsx3

engine = pyttsx3.init()

while True:
	anwser = input("enter naything: ")
	engine.say(anwser)
	engine.runAndWait()
