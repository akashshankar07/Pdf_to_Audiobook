import pyttsx3

try:
    tts_engine = pyttsx3.init()
    #tts_engine.save_to_file('the text I want to save as audio',r"C:\Users\91990\Desktop\textspeech")
    #AudioSegment.from_file(r"C:\Users\91990\Desktop\textspeech").export('converted.mp3', format="mp3")
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        print(voice.name)
    print(voices)
    tts_engine.setProperty('voice', voices[0].id)
    tts_engine.say('This is just a test.')
    tts_engine.runAndWait()
    input('Press enter to exit.')
except:
    print('error')