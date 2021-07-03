# Pdf_to_Audiobook

Libraries used:

pyttsx3
It is an open source library that invokes Microsoft speech to text recognition software to convert the texts to speech synthesis.

After construction, it uses the engine object to register and unregister event callbacks; produce and stop speech.
The pyttsx3.voice class contains information about the speech synthesizer voice.

Working:

The given pdf file is read from the given directory.
Using PyPDF2, we take the pdf and convert it into strings.
It is further broken down into words using looping methods and then the engine.say() function is called to read aloud the words.
This way all the words of the PDF file is traversed.
The voice can be set again as Male or Female(Zira) based on in-built Microsoft libraries to be invoked.
Further modifications can also be done to change the rate of speech, i.e, the words per minute and volume level can be changed. 


Saving of the file to audio format:

The engine.save_to_file() can be used to save the given speech in an audio format
The format can be specified by the user as .mp3 or .wav
The file is saved in the working directory of the project or any other directory as specified.
It can be used to listen to the audio file later for other purposes.
Also, from the PyDub library AudioSegment can be imported and it can be used as an alternative way to store the speech in the working directory specified.

AudioBook.py is the primary program file.

Sample files for checking have been included sich as Poem1, Short_story_1

ad1,ad2 are sample audio .wav files generated from the respective documents aforementioned
