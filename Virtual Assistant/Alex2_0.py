# Author : Azim Ahmed Bijapur,Arkaan Khan,Rohan Bhabal,Abuzar Sheikh
# Institution :M.H.Saboo Siddik College Of Engineering
# Second Year Mini Project
# Year 2021-22

import pyttsx3
import random
import tkinter
import datetime
import speech_recognition as sr
import webbrowser
import windowsapps
import wolframalpha
import time
from PIL import ImageGrab
import os
import screen_brightness_control
import keyboard
import sys
def close():
   sys.exit()
try:
   import pywhatkit
except:
   window=tkinter.Tk()
   window.lift()
   window.eval('tk::PlaceWindow . center')
   window.title("Warning")
   window.config(height=200,width=435)
   warn=tkinter.Label(window,text="No Internet Connection!!",font="Calibri 20")
   warn.place(x=50,y=50)
   window.mainloop()
   exit()

# Setting up the tts engine

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)

# Wish at the beginning

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alex Sir. Please tell me how may I help you") 

# Making it speak

def speak(audio):
    engine.say(audio)
    try:
      engine.runAndWait()
    except Exception as e:
       print("nothing much")

# Take voice input

def takeCommand():
      
     r=sr.Recognizer()
 
     with sr.Microphone() as source:
          
         r.energy_threshold=400
          
         r.dynamic_energy_threshold=False

         print("Listening...\n")

         audio=r.listen(source)

         try:

             print("Recognizing...\n")

             audio = r.recognize_google(audio, language='en-in')
              
             query=audio.lower()         

             print(query+"\n")  
              
         except Exception as e:
             
               query=""

               print("Sorry ")
         
         # Execute based on the input

         if 'type' in query:

            sentence=query.replace('type','')

            keyboard.write(sentence)
         
         elif 'are you' in query:

            speak("Go ahead I am listening to you")

         # Wolframalpha api used here

         elif 'tell me' in query:
            speak('Always here to answer your questions,give me a second')
            client = wolframalpha.Client('GRL2AR-KL6GUV7K2R')
            question=query.replace("tell me","")
            print(question)
            res = client.query(question)
            try:
               answer = next(res.results).text
               speak(answer)
            except Exception as e:
               speak("I did not understand that question")

         # Web based commands

         elif 'search' in query:
            sentence=query.replace("youtube","")
            try:
               pywhatkit.search(sentence)
               speak("Searching")
            except:
               speak("Network Error Occured")
         
         elif 'youtube' in query:

            sentence=query.replace("youtube","")

            try:
               pywhatkit.playonyt(sentence)
               speak("Playing...")
            except:
               speak("Network Error Occured")
         

         elif 'news' in query:
             
            speak("showing you some fresh news ")
             
            webbrowser.open("https://www.youtube.com/c/BBCNews")

             

         elif 'drive' in query:
             
            speak("opening google drive ")
             
            webbrowser.open("https://drive.google.com/drive/my-drive")

             

         elif 'meet' in query:
             
            speak("opening google meet ")
             
            webbrowser.open("https://meet.google.com/")
        
             

         elif 'game' in query:
             
            speak("As you wish ")
             
            webbrowser.open("https://chromedino.com/")

             
         
         elif 'github' in query:
             
            speak("opening github ")
             
            webbrowser.open("https://github.com/")
         

         elif 'whatsapp' in query:
             
            speak("opening whatsapp , please wait")
             
            webbrowser.open("https://web.whatsapp.com")
             
             

         elif 'mail' in query:
             
            speak("opening gmail ")
             
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")


         elif 'fiddle' in query:
             
            speak("opening sql fiddle ")
             
            webbrowser.open("https://www.db-fiddle.com/f/6GJsV5KP3csKy9vg4y2us7/0")
             
             

         elif 'classroom' in query:
             
            speak("opening google classroom ")
             
            webbrowser.open("https://classroom.google.com/h")
             

         elif 'weather' in query:
             
            speak("showing weather news ")

            webbrowser.open("https://www.bing.com/search?q=weather&cvid=80b3646d80b745f3808c8e0549263256&aqs=edge.0.0l9.3156j0j1&pglt=43&FORM=ANSPA1&PC=EDGEDB") 

         #Internet speed test        

         elif 'internet speed' in query:
            
            speak("checking internet speed")

            webbrowser.open("https://www.speedtest.net/")
         
         #What's the time?

         elif 'time' in query:
             
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

         #System commands I

         elif 'increase brightness' in query:
            current=screen_brightness_control.get_brightness()
            screen_brightness_control.set_brightness(current+10)
            if current==100:
               speak("Maximum brightness")
            else:
               speak("Increased")

         elif 'reduce brightness' in query:
            current=screen_brightness_control.get_brightness()
            screen_brightness_control.set_brightness(current-10)
            if current==0:
               speak("Minimum brightness")
            else:
               speak("Decreased")
         
         elif 'xbox' in query:
            if(windowsapps.find_app('xbox game bar')=="Application not found!"):  
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('xbox game bar')               
               speak("Opening xbox game bar")      


         elif 'word' in query:
            if windowsapps.find_app('Word')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               speak("opening word ")
               windowsapps.open_app("Word")
         
         # Making it take Screenshot

         elif 'screenshot' in query:
            try:
               image = ImageGrab.grab(all_screens=True)
               i=random.randint(0,10000)
               image.save(f'C:\Screenshots\\sc{i}.png')    
               speak("Taken")
            except Exception as e:
               speak('retake the screenshot')

         elif 'powerpoint' in query:
             
            if windowsapps.find_app('Powerpoint')=="Application not found!":
               speak("You do not have this application")
                
            else: 
                
               speak("opening power point")
               windowsapps.open_app("Powerpoint")
         
         elif 'calculator' in query:
             
            if windowsapps.find_app('calculator')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('calculator')
               speak("Opening calculator")
                
         elif 'camera' in query:
             
            if windowsapps.find_app('camera')=="Application not found!": 
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('camera')
               speak("Opening camera")
                
         elif 'zoom' in query:
             
            if windowsapps.find_app('zoom')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('zoom')
               speak("Opening zoom")
                
         # Browsers

         elif 'edge' in query:
            if windowsapps.find_app('Edge')=="Application not found!":
               speak("You do not have this application")
                
            else: 
                
               speak("opening Microsoft Edge")
               windowsapps.open_app("Edge")

         elif 'chrome' in query:
             
            if windowsapps.find_app('chrome')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('chrome')
               speak("Opening google chrome")
         
         elif 'firefox' in query:
             
            if windowsapps.find_app('firefox')=="Application not found!": 
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('firefox')
               speak("Opening firefox")
                
         # Take some notes
      
         elif 'remember that' in query:
            
            qa=query
            remeberMsg = qa.replace("remember that ","")
            speak("okay I will remember that :")
            try:
               remeber = open('memory.txt','w')
               remeber.write(remeberMsg)
               remeber.close()
            except:
               speak("memory file is missing , create a memory text file where i am placed")

         elif 'what do you remember' in query:
            try:
               remeber = open('memory.txt','r')
               speak("You told me that:" + remeber.read())
               remeber.close()
            except:
               speak("memory file is missing , create a memory text file where i am placed")
             

         # System commands II

         elif 'eclipse' in query:
             
            if windowsapps.find_app('eclipse')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('eclipse')
               speak("Opening eclipse")
                
             

         elif 'intellij' in query:
             
            if windowsapps.find_app('intellij idea')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('intellij idea')
               speak("Opening intellij idea")
                
             

         elif 'paint' in query:
             
            if windowsapps.find_app('paint')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('paint')
               speak("Opening paint")
                
         elif 'notepad' in query:
             
            if windowsapps.find_app('notepad')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('notepad')
               speak("Opening notepad")
                
         elif 'excel' in query:
             
            if windowsapps.find_app('excel')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('excel')
               speak("Opening excel")
                
         elif 'picture' in query:
             
            if windowsapps.find_app('photos')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('photos')
               speak("Opening photos")
                
         elif 'control panel' in query:
             
            if windowsapps.find_app('control panel')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('control panel')
               speak("Opening control panel")

         elif 'play music' in query:
             
            speak("Opening media player")
            windowsapps.open_app("windows media player")

         elif 'photoshop' in query:
             
            if windowsapps.find_app('adobe photoshop')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('adobe photoshop')
               speak("Opening adobe photoshop")
                
         elif 'to do' in query:
             
            if windowsapps.find_app('to do')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('to do')
               speak("Opening microsoft to do")
             
         elif 'your phone' in query:
             
            if windowsapps.find_app('your phone')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('your phone')
               speak("Opening your phone")
         
         elif 'calendar' in query:
            if windowsapps.find_app('calendar')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('calendar')
               speak("Opening calendar")
             
         # Commands Line utilities

         elif 'powershell' in query:
             
            if windowsapps.find_app('powershell')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('powershell')
               speak("Opening windows powershell") 
             

         elif 'bash' in query:
             
            if windowsapps.find_app('git bash')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('git bash')
               speak("Opening git bash")
             
         # Programming 

         elif 'python' in query:
            if windowsapps.find_app('IDLE (Python 3.10 64-bit)')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('IDLE (Python 3.10 64-bit)')    
               speak("Opening python shell")
         
         elif 'android studio' in query:
            if windowsapps.find_app('android studio')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('android studio')
               speak("Opening android studio")
         
         elif 'code' in query:
            if windowsapps.find_app('Visual Studio Code')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               speak("opening Visual studio code , please wait")
               windowsapps.open_app("Visual Studio Code")
         

         # Video Editting software

         elif 'filmora' in query:
             
            if windowsapps.find_app('filmora')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('filmora')
               speak("Opening filmora")
             

         elif 'premiere' in query:
             
            if windowsapps.find_app('adobe premiere pro')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('adobe premiere pro')
               speak("Opening adobe premiere pro")
      
      # Vital system commands
         
         elif 'power of' in query:
            speak("Logging of the computer in 5 seconds")
            time.sleep(5)
            os.system("shutdown /s /t 1")

         elif 'sleep' in query:
            speak("As you wish")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

         elif 'restart' in query:
            speak("As you wish")
            os.system("shutdown /r /t 0")

      # Final block    
            
         elif 'quit' in query:
            speak("Have a nice day")
            sys.exit()   
            
         else:
            query=""
            speak("")

       
wishMe()
        
while(True):
        
   takeCommand()

# End of Code
    
     

