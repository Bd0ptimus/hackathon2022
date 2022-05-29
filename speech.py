import speech_recognition as sr
#import pyttsx3
r=sr.Recognizer();

#Function to convert text to speech

#def SpeakText(command):
#	engine=pyttsx3.init()
#	engine.say(command)
#	engine.runAndWait();

with sr.Microphone(device_index=1) as source:
	print('Speak anything:')
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source,2)

try:
   	Text=r.recognize_google(audio,language='ru-RU')
   	print("Converted Audio Is : \n "+Text)
except Exception as e:
    print("Error : {} ".format(e) )