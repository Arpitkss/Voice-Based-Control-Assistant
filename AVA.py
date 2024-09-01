import pyttsx3
import speech_recognition as sr
import os
import subprocess as sp
import datetime
import calendar
import wikipedia
import smtplib
import webbrowser as wb
import pyscreenshot
import psutil
import time
import pyjokes
import random
import requests
import json
import wolframalpha
import sys
#
import snake1 as sn
import pong5 as po
import take_pic as tp
import take_vid as tv
import detect_face_video as dfv
import detect_face_image as dfi


# Funtion which makes the Assistant speak

def respond(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take commands form microphone

def takeInput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('.'*20)
        print(".............Listening.............")
        r.pause_threshold=1
        r.energy_threshold=3000
        audio=r.listen(source)
    try:
        print(">>>>.........Recognizing...........")
        print('.'*20)
        query=r.recognize_google(audio,language='en-in')
        #os.system('cls')
    
    except Exception as e:
        #print(e)
        respond("Sorry I didn't get that can you please repeat.........")
        return "Nothing"
    return query

'''
def takeInput():
    print("Listening.....")
    print(">>.........Recognizing.........")
    x=input('user said : ')
    return x
'''

def title():
    print("*"*80)
    print("\n\t\tVOICE BASED CONTROL SYSTEM & ASSISTANT\n")
    print("*"*80)
    print("\t\t\tVersion 1.0\n")
    print("NOTE : say 'Go Offline' or 'Exit System' to close this application")
    print("*"*80,end='\n\n')

# Function for greetings

def greeting():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        respond("Good Morning Sir")
    if hour>=12 and hour<16:
        respond("Good Afternoon Sir")
    if hour>=16 and hour<=24:
        respond("Good Evening Sir")
    
    respond("I am your PC virtual assistant at your service. How Can I help you Sir")


# Function to tell Date

def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th','14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd','23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    print('\nToday is ' + weekday + ', ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1])
    respond('Today is ' + weekday + ', ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1])
    # year=int(datetime.datetime.now().year)
    # month=int(datetime.datetime.now().month)
    # date=int(datetime.datetime.now().day)
    # respond("The current date is")
    # respond(date)
    # respond(month)
    # respond(year)


# Function to tell Time

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    respond("Current time is...")
    print("\nCurrent time : "+Time)
    respond(Time)
    
    
# funtion to tell about CPU percentage

def cpu():
    usage=str(psutil.cpu_percent())
    print("CPU is at" + usage +'% usage')
    respond("CPU is at" + usage)


# function to tell battery percentage
def battery():
    try:
        battery=psutil.sensors_battery()
        respond("\nbattery is at")
        print(battery.percent,end='')
        print(' %')
        respond(battery.percent)
        respond("percent")
    except:
        print("No battery found !!")
        respond("no battery found. Seems like you are on a desktop sir.")

# Function to tell joke

def jokes():
    pj=pyjokes.get_joke()
    print('\n'+pj)
    respond(pj)


# function to take screenshot

def screenshot():
    img = pyscreenshot.grab()        
    img.show()           
    img.save("ss.png")


# Function to send Emails

def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()#to send email
    server.login("kb28code@gmail.com","kushagra*123#")
    server.sendmail('kb28code@gmail.com',to,content)
    server.close()


# Function to tell news

def news():

    url = (f"http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e38e33aa03d448068b70c4c1c2fed2f4")

    response = requests.get(url)
    t = response.text
    my_json = json.loads(t)
    respond("News for the day are")
    for i in range(0, 5):
        print('\n'+my_json['articles'][i]['title'])
        respond(my_json['articles'][i]['title'])        
        #respond("the description of above news is" + my_json['articles'][i]['description'])


# Function to tell features

def features():

    f=['Tell time','Tell date','Tell a Joke','Search things in Wikipedia',
       'Send Emails through Gmail','Search online','Search in YouTube',
       'Shutdown the System','Logout the System','Restart the System',
       'Hibernate the system','Play songs','Switch Songs',
       'Play Videos','Switch Videos','Remember things',
       'Tell what you told me to remember','Take Screenshots','Tell about CPU status',
       'Tell battery Percentage','Tell News','Open System applications',
       'Launch Classic games','Take Pictures and record videos','and a lot more' ]
    
    print('\n')
    respond("I can..")
    for i in f:
        print(i)
    for i in f:
        respond(i)


#Function to answer questions

def answer():
    question =query
    app_id = 'ERH22X-RQJH8HR55T'
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(question)
        answer = next(res.results).text
        print('\n'+answer)
        respond(answer)
    except:
        print('No results found for this...')
        respond('I am unable to find answer for this;')
        respond('Would you like to search this online sir?')
        x=takeInput()
        if 'yes' in x or 'sure' in x or 'yeah' in x or 'ok' in x:
            wb.open_new_tab("https://www.google.co.in/search?q="+query)
            respond('here you go sir')
        else:                
            respond('ok')
                
    
    
    

#-------------------------------------------------------------------------------------
#                               M A I N     F U N C T I O N
#-------------------------------------------------------------------------------------



# Control System Main function



if __name__ == '__main__':
    
    engine=pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.setProperty('volume',0.75)
    
    title()
    greeting()
    
    while True:
        try:
            query=takeInput().lower()
            print('\n-------\n'+'I heard : '+query)
            
            if 'do not' in query or 'dont' in query or "don't" in query or 'never' in query or 'not to' in query:
                respond("ok. i got it ! no such action will be performed sir ! Ha Ha ha!")
            
            elif "date" in query and 'update' not in query:
                date()
            
            elif "time" in query:
                time_()
            
            elif 'screenshot' in query:
                screenshot()
                respond("Screenshot taken")

            elif 'cpu' in query:
                cpu()
            
            elif 'battery' in query:
                battery()
            
            elif 'joke' in query:
                jokes()
            
            elif 'news' in query:
                news()
            
            # creating folder
            elif (("create" in query or ("make" in query)) and  ("folder" in query or "directory" in query)):
                #parent_dir=input("-----> ")
                print("Give a name to the folder.")
                respond("give a name to the folder")
                name=takeInput()
                #directory=input("-----> ")
                try:
                    path=(os.getcwd())
                    folder=os.path.join(path,name)
                    os.mkdir(folder)
                    print("OK,Creating the folder called "+name+ " in " +os.getcwd())
                    respond("OK, Creating the folder called "+name+ " in current directory")
                except:
                    print("Folder already exists")
                    respond("Folder already exists")
                            
            
            
            # description of Features of the assistant
            elif('what can you do' in query or 'what are your' in query and ('features' in query or 'abilities' in query or 'capabilities' in query)):
                features()
            
            # weather update online
            elif 'weather' in query:
                wb.open_new_tab('https://www.google.co.in/search?q=weather+update')
            
            #for searching in wikipedia
            elif "wikipedia" in query:
                try:
                    respond("Sure sir. please say the topic name only; that you want to search about")
                    wikiquery=takeInput()
                    
                    wikiquery=wikiquery.replace("wikipedia","")
                    print('I heard : '+wikiquery)
                    result=wikipedia.summary(query,sentences=2)
                    print(result)
                    respond(result)
                except:
                    print('\nDue to some technical issues i am unable to get results!')
                    respond('Due to some technical issues i am unable to get results!')
                    print('\n\n---- Search online or this ??')
                    respond('Would you like to search this online sir?')
                    x=takeInput()
                    if 'yes' in x or 'sure' in x or 'yeah' in x or 'ok' in x:
                        wb.open_new_tab("https://www.google.co.in/search?q="+wikiquery)
                        respond('here you go sir')
                    else:                
                        respond('ok')
                    
            #for sending email
            elif 'send' in query and ('email' in query or 'mail' in query):         
                try:
                    respond("What should I say")
                    content=takeInput()
                    print('message : '+content+'\n')
                    respond("Please type in the receiver's email address")
                    to=input('email address : ')
                    sendmail(to,content)
                    print('\nEmail sent successfully.\n')
                    respond("Email sent successfully")
                except Exception as e:
                    # print(e)
                    # respond(e)
                    print("\nUnable to send email.")
                    respond("Unable to send the email")
            
            elif 'my' in query and ('mail' in query or 'mails' in query or 'inbox' in query):
                wb.open_new_tab('https://mail.google.com/mail/u/0/#inbox')
                
            elif 'search' in query or (('find' in query or 'play' in query) and ('internet' in query or 'web' in query or 'online' in query or 'something' in query)):
                respond("What should I search for")
                #chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                search=takeInput().lower()
                wb.open_new_tab('https://www.google.co.in/search?q='+search)
            
            # open youtube
            elif (("run" in query) or ("execute" in query) or ("on" in query) or ("open" in query)) and ("youtube" in query):
                print("\nStarting YouTube....")
                respond("starting youtube")
                respond("What do you want to open ?")
                search=takeInput().lower()
                wb.open_new_tab("https://www.youtube.com/results?search_query="+search)
            
            # logout pc
            elif 'logout' in query and ('system' in query or 'computer' in query or 'pc' in query):
                respond('you sure want to logout sir ?')
                x=takeInput()
                if 'yes' in x or 'sure' in x or 'yeah' in x:
                    os.system("shutdown - l")  #for logout 
                else: respond('ok')
            
            # shutdown pc
            elif 'shutdown' in query and ('system' in query or 'computer' in query or 'pc' in query):
                respond('you sure want to shutdown your computer sir ?')
                x=takeInput()
                if 'yes' in x or 'sure' in x or 'yeah' in x:
                    os.system("shutdown /s /t 1")  #for shutdown 
                else: respond('ok')
            
            # restart pc
            elif 'restart' in query and ('system' in query or 'computer' in query or 'pc' in query):
                respond('you sure want to restart your computer sir ?')
                x=takeInput()
                if 'yes' in x or 'sure' in x or 'yeah' in x:
                    os.system("shutdown /r /t 1")  #for restart 
                else: respond('ok')
            
            # put pc to sleep
            elif 'sleep' in query and 'mode' in query and ('system' in query or 'computer' in query or 'pc' in query):
                respond('you sure want to restart your computer sir ?')
                x=takeInput()
                if 'yes' in x or 'sure' in x or 'yeah' in x:
                    os.system("shutdown /r /t 1")  #for restart 
                else: respond('ok')
            
            # to change desktop background
            #elif 'change background' in query:
            #    ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
            
            # to play song
            elif "play" in query and "song" in query:
                songs_dir="D:/Music"
                songs=os.listdir(songs_dir)
                n=random.randint(0,len(songs)-1)
                os.startfile(os.path.join(songs_dir,songs[n]))
            
            # to switch songs
            elif (("play another" in query or 'switch' in query or 'change' in query) and ("song" in query or 'songs' in query)):
                respond("Ok sir: Playing another song.")
                songs_dir="D:/Music"
                songs=os.listdir(songs_dir)
                n=random.randint(0,len(songs)-1)
                p=os.startfile(os.path.join(songs_dir,songs[n]))
            
            # to play video
            elif "play video" in query:
                vids_dir="D:/Videos"
                vids=os.listdir(vids_dir)
                n=random.randint(0,len(vids)-1)
                os.startfile(os.path.join(vids_dir,vids[n]))
            
            # to play another video
            elif (("play another" in query or 'switch' in query or 'change' in query) and ("video" in query or 'videos' in query)):
                respond("Ok sir: Playing another video.")
                vids_dir="D:/Videos"
                vids=os.listdir(vids_dir)
                n=random.randint(0,len(vids))
                os.startfile(os.path.join(vids_dir,vids[n]))
            
            # to make assistant to remember something

            elif "remember" in query and ('something' in query or 'that' in query) or 'reminder' in query:
                respond("What should I remember")
                data=takeInput()
                respond("you said me to remember, " + data)
                remember=open("reminder.txt","w")
                remember.write(data)
                remember.close()
                respond('reminder saved !')
                    
            # make assistant speak what you told to remember
            elif 'to remember' in query:
                remember=open("reminder.txt","r")
                respond("you said me to remember, " + remember.read())
                print('\nReminder Saved Successfully!')
            
            # to show reminder data text    
            elif "show" in query and ('reminder' in query ):
                respond("Showing Reminder text")
                os.startfile(os.path.join(os.getcwd(), 'reminder.txt'))
            
            
            # to compose a note from voice and save it
            elif "write" in query and "note" in query:
                respond("What should i write sir?")
                note = takeInput()
                file = open('note.txt', 'w')
                respond("Sir, Should i include date and time")
                x = takeInput()
                if 'yes' in x or 'sure' in x or 'ok' in x:
                    strTime = datetime.datetime.now().strftime("%I:%M:%S")
                    file.write(strTime)
                    file.write(" :- \n")
                    file.write(note)
                    file.write('\n----------------')
                else:
                    file.write(note)
                    print("\nNote Saved !")
                    respond("note Saved")
             
            elif "show" in query and ('note' in query or "notes" in query):
                respond("Showing Notes")
                os.startfile(os.path.join(os.getcwd(), 'note.txt'))
                #file = open("note.txt", "r")
                #print(file.read())
                #respond(file.read(6))
            
            
            # game files' execution
            
            elif 'snake' in query and 'game' in query:
                sn.snake()
                #sp.Popen('python snake1.py')
            
            elif 'pong' in query and 'game' in query:
                po.pong()
                #sp.Popen('python pong5.py')
            
            
            
            # open camera to capture picture
            elif ('open camera' in query or 'open webcam' in query or 'open web cam' in query or (('take' in query) and ('photo' in query or 'picture' in query))):
                tp.pic()
                #sp.Popen('python take_pic.py')
            
            # open camera to record video
            elif(('take' in query or 'capture' in query or 'record' in query) and 'video' in query):
                tv.vid()
                #sp.Popen('python take_vid.py')
            
            # for image face detection
            elif((('detect' in query or 'detection' in query or 'find' in query) and ('face' in query or 'faces' in query)) and ('image' in query or 'photo' in query or 'picture' in query)):
                respond('here you go')
                dfi.detect()
            
            # for real-time face detection
            elif(('detect' in query or 'detection' in query or 'find' in query) and ('face' in query or 'faces' in query)):
                respond('Let me try')
                dfv.detect()
            
            
            # to open system apps
            
            elif('calculator' in query or 'calc' in query):
                sp.Popen('C:\\Windows\\System32\\calc.exe')
                respond('opening calculator')
            elif('notepad' in query):
                sp.Popen('C:\\Windows\\System32\\notepad.exe')
                respond('opening notepad')
            elif('mozilla' in query or 'firefox' in query):
                sp.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            elif('google' in query or 'chrome' in query):
                sp.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe abc.com")
                respond('opening Google Chrome')
            elif('vlc' in query or 'v l c' in query or 'media player' in query):
                sp.Popen('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe')
                respond('opening VLC, media player')
            elif('media player' in query or 'video player' in query):
                sp.Popen('wmplayer')
                respond('opening windows media player')
            elif('cmd' in query or 'command line' in query or 'terminal' in query or 'command prompt' in query):
                sp.Popen('C:\\Windows\\System32\\cmd.exe')
                respond('opening windows command prompt')
            elif('wordpad' in query):
                sp.Popen('C:\\Windows\\System32\\write.exe')
                respond('opening wordpad')
            elif('control panel' in query):
                sp.Popen('C:\\Windows\\System32\\control.exe')
                respond('opening control panel')
            elif('mycomputer' in query or 'my computer' in query or 'explorer' in query or 'computer' in query):
                os.system('start explorer shell:mycomputerfolder')
                respond('opening my computer folder')
            elif('magnifier' in query):
                sp.Popen('C:\\Windows\\System32\\magnify.exe')
                respond('opening magnifier')        
            elif('paint' in query):
                sp.Popen('C:\\Windows\\System32\\mspaint.exe')
                respond('opening MS paint')
        
            # Default windows games
            
            elif('chess' in query and 'game' in query):
                sp.Popen('C:\\Program Files\\Microsoft Games\\Chess\\chess.exe')
                respond('opening Microsoft Chess Game')
            
            elif(('purble' in query or 'purple' in query) and 'Place' in query and 'game' in query):
                sp.Popen('C:\\Program Files\\Microsoft Games\\Purble Place\\PurblePlace.exe')
                respond('opening Microsoft Purble Place Game')
            
            elif('mine' in query and 'sweeper' in query and 'game' in query):
                sp.Popen('C:\\Program Files\\Microsoft Games\\minesweeper\\minesweeper.exe')
                respond('opening Microsoft Mine Sweeper Game')
            
            elif('solitaire' in query and 'game' in query):
                sp.Popen('C:\\Program Files\\Microsoft Games\\minesweeper\\Solitaire.exe')
                respond('opening Microsoft Solitaire Game')
            
            
            
            elif "don't listen" in query or "stop listening" in query or 'sleep' in query:
                respond("Going to sleep for 10 seconds sir")
                print('!!!!  Sleep Break !!!!\n.....Not Listening for 10 seconds..... ')
                time.sleep(10)
                print('__'*10+'\n!!! Awake Now !!!\n'+'__'*10)
                respond('I am Awake Now Sir')
                
            elif 'who are you' in query:
                respond('I am your PC digital virtual Assistant sir. Althogh I have no name, but you can name me anything.')
                print('I am your PC digital virtual Assistant.\n\nAlthogh I have no name, but you can name me anything.\n\n')
                
            elif 'how are you' in query:
                respond('I am fine sir. Thankn you ! How are you Sir ?')
                print('\n\nI am fine sir. Thankn you ! How are you Sir ?\n\n')
                
            elif 'who are you' in query:
                respond('I am your PC digital virtual Assistant sir. Althogh I have no name, but you can name me anything.')
                print('I am your PC digital virtual Assistant.\n\nAlthogh I have no name, but you can name me anything.\n\n')
            
            
            
            elif 'what' in query or 'where' in query or 'who' in query or 'when' in query:
                answer()
            
            ## EXIT and STOP EXECUTION
            elif "offline" in query or "stop execution" in query or 'exit system' in query or "go away" in query:
                respond("ok Sir! I am taking my leave. Thank you.")
                sys.exit("\n\n"+'##'*40)
            
            elif 'nothing' in query:
                print()
            else:
                print('\n Please Try Again !')
                respond('Sorry I did not find anything related to this ! Please try again sir.')
        except :
            print("")
