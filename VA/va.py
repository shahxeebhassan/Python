import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pandas
import pyaudio
import tkinter as tk
import openai
from gtts import gTTS
import playsound
import time
from googletrans import Translator

translator = Translator()
listener = sr.Recognizer()
engine = pyttsx3.init()

openai.api_key = "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"

# root = tk.Tk()
# root.title("Virtual Assistant")
# root.geometry("4000x4000")

# create a label for the output
# output_label = tk.Label(root, text="I am your virtual assistant. What can I do for you?", font=("Arial", 44), wraplength=1000, justify="center")
# output_label.pack(pady=20)

# create a function to activate the virtual assistant
# def activate_assistant():
# #     button.config(text="Listening...", bg="green", state="disabled")
#     command = take_command()
#     print(command)
#     button.config(text="Activate Assistant", bg="SystemButtonFace", state="normal")

# create a function to get voice command from user
def take_command():
    while (1):
        try:
            with sr.Microphone() as source:
                # print('listening...')
#             button.config(text="Listening...", bg="green", state="disabled")
                talk("Listening")
            # offlineSpeak("Listening")
                listener.adjust_for_ambient_noise(source, duration=0.5)

            # listens for the user's input
                audio2 = listener.listen(source)

            # Using google to recognize audio
                command = listener.recognize_google(audio2)
                command = command.lower()
                print(command)
                eng = translator.translate(command, dest='en')
                command = eng.text.lower()
                # lan=translator.detect(MyText)
                # if lan.lang == 'ur' or lan.lang == 'hi':
                    # command = eng.text.lower()
                print(command)
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
                
                if 'play' in command:
                    song = command.replace('play', '')
                    talk('playing ' + song)
                    pywhatkit.playonyt(song)
                
                elif 'open folder' in command:
                    folder_path = '/path/to/folder' # replace with actual folder path
                    os.startfile(folder_path)
                
                elif 'link' in command:
                    query = command.replace('link', '')
                    talk(f"Here's the link for {query}")
                    search_result = pywhatkit.search(query)
                    webbrowser.open(search_result)
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    # urdu= translator.translate("", dest='ur')
                    talk("Is waqt ka time hai " + time)
                elif 'who is' in command:
                    person = command.replace('who is', '')
                    info = wikipedia.summary(person, 1)
                    urdu= translator.translate(info, dest='ur')
                    print(info)
                    talk(urdu.text)
                elif 'date' in command:
                    urdu= translator.translate("I am in a relationship with wifi", dest='ur')
                    talk(urdu)
                elif 'are you single' in command:
                    urdu= translator.translate("I am in a relationship with wifi", dest='ur')
                    talk(urdu.text)
                elif 'joke' in command:
                    talk(pyjokes.get_joke())
                else:
                # Only call OpenAI if none of the above conditions are met
                    response = generate_response(command)
                    urdu= translator.translate(response, dest='ur')
                    print(response)
                    talk(urdu.text)
#                 button.config(text="Activate Assistant", bg="SystemButtonFace", state="normal")
        except:
            pass

#     return command


# create a function to generate response using OpenAI API
def generate_response(prompt):
    completions = openai.Completion.create(
        model = "text-davinci-003",
#         engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        temperature=0.9,
        
    )
    message = completions.choices[0].text.strip()
    return message

# create a function to output the response from the virtual assistant
def offlineTalk(text):
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()
#     output_label.configure(text=text)
def talk(audio_string): 
    tts = gTTS(text=audio_string, lang='ur') # text to speech(voice)
    audio_file = 'audio-' + str() + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    # print(audio_string) # print what app said
    os.remove(audio_file) # remove audio file

take_command()
# create a button to activate the virtual assistant
# button = tk.Button(root, text="Activate Assistant", command=activate_assistant)
# button.pack()

# root.mainloop()