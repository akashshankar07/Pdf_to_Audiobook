import pyttsx3
import pdfplumber
import PyPDF2

file = 'Poem1.pdf'
#file object
pdfFileObj = open(file, 'rb')
#file reader object
pdfReader= PyPDF2.PdfFileReader(pdfFileObj)
#no of pages
pages = pdfReader.numPages
engine = pyttsx3.init()
speaker = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
volume = engine.getProperty('volume')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-20)
engine.setProperty('volume',volume+0.5)
"""for voice in voices:
    engine.setProperty('voice',voice.id) """
#loop no of pages in pdf file
#extracting text from the pages 
with pdfplumber.open(file) as pdf:

    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        
        speaker.say(text)
        speaker.save_to_file(text,'ad2.wav')
        speaker.runAndWait()

