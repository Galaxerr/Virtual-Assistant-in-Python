import speech_recognition as sr
import webbrowser  
import datetime  
import wikipedia 
from ttsvoice import tts
from calculator.simple import SimpleCalculator

 
 
# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():
 
    r = sr.Recognizer()
 
    # from the speech_Recognition module 
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')
         
        # seconds of non-speaking audio before 
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
         
        # Now we will be using the try and catch
        # method so that if sound is recognized 
        # it is good else we will have exception 
        # handling
        try:
            print("Recognizing")
             
            # for Listening the command in indian
            # english we can also use 'hi-In' 
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
             
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
         
        return Query
 
def speak(audio):
    tts(audio)  
 
def tellDay():
     
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
     
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

 
def tellTime():
     
    # This method will give the time
    time = str(datetime.datetime.now())
     
    # the time will be displayed like 
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")    
 
def Hello():
     
    # This function is for when the assistant 
    # is called it will say hello and then 
    # take query
    speak("hello sir I am your desktop assistant. Tell me how may I help you")
 
 
def Take_query():
 
    # calling the Hello function for 
    # making it more interactive
    Hello()
     
    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate 
    # the program
    while(True):
         
        # taking the query and making it into
        # lower case so that most of the times 
        # query matches and we get the perfect 
        # output
        query = takeCommand().lower()
        if "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "open" and "youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue
             
        elif "which day is it" in query:
            tellDay()
            continue
         
        elif "tell me the time" in query:
            tellTime()
            continue

        elif "calculate" in query:
            result=SimpleCalculator()
            result.run(str(query))
            speak("The answer is " + str(result.lcd))
            print("The answer is " + str(result.lcd))
            continue

        elif "from wikipedia" or "on wikipedia" or "what is" in query:
             
            # if any one wants to have a information
            # from wikipedia
            query = query.replace("wikipedia", "")
             
            # it will give the summary of 4 lines from 
            # wikipedia we can increase and decrease 
            # it also.
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            speak(result)
            continue
         
        elif "tell me your name" in query:
            speak("I am just a Test, I don't have a name yet, but I'm your desktop Assistant")
            continue
        
        # this will exit and terminate the program
        elif "quit" or "bye" or "exit" in query:
            speak("Pleasure to be of service, until next time")
            exit()
 
if __name__ == '__main__':
    # main method for executing
    # the functions
    Take_query()