import pyttsx3
engine = pyttsx3.init()
rate= engine.getProperty('rate')
engine.setProperty('rate',140)
volume = engine.getProperty('volume')
print(volume)
voices = engine.getProperty('voices')

engine.say("Hello Akash, its Jarvis here")
engine.say('My current speaking rate is '+ str(rate))
engine.runAndWait()
engine.stop()
