from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import views.Index_Avatar
import main
import threading
import time
import winsound
import pyautogui
from bs4 import BeautifulSoup
import requests
import string
import random
import cv2
import datetime
from GoogleNews import GoogleNews
import os
import signal
from AppOpener import run, give_appnames
import winapps
from difflib import get_close_matches
import datetime
import pyjokes
import pywhatkit as kit
import subprocess
import wolframalpha
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import wikipedia
import FaceReg


    
class Assistant:
    
    
    
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        
        self.message = ''
        self.result = ''
        self.lengthoftext = ''
        self.appList = []
        self.currentUser = ''
        
        for app in winapps.list_installed():
            ap = app.name
            ap = ap.lower()
            self.appList.append(ap)	
            
        
        self.mappings = {
            "greeting": self.hello,
            # "create_note": self.create_note,
            # "add_todo": self.add_todo,
            "show_todo": self.show_todo,
            "about": self.about,
            "news": self.readNews,
            "exit": self.quit,
            "photo":self.takePhoto,
            "screenshot": self.screenshot,
            "open":self.appstart,
            "time":self.time,
            "joke":self.tellJoke,
            "write":self.writeOnScreen,
            "youtube":self.watchYoutube,
            "maths":self.doMath,
            "weather":self.getWeather,
            "thanks":self.thanks,
            "food":self.food,
            "marriege":self.marriege,
            "sports":self.sports,
            "sad":self.sad,
            "help":self.help,
            "i_love_you":self.loveU,
            "wswitch":self.switch,
            "guessMe":self.guessWho,
            "image":self.image,
            "deafult": self.tryWolframaalpha,
        }
        self.assistant = GenericAssistant('intents.json', intent_methods=self.mappings )
        self.assistant.train_model()
        self.currentUser = FaceReg.startRecognitiion()
        self.startSplashScreen()
        
        # self.startAssistant()
    
    def onWord(self, name, location, length):
        value = location + length
        if value == self.lengthoftext:
            print("onWord done")
            views.Index_Avatar.stopTalk()
            
    

    def speak(self,text):
        print("start")
        engine = tts.init()
        engine.connect('started-word', self.onWord)
        engine.setProperty('rate', 150)
        views.Index_Avatar.startTalk()
        # ui.promptController(self.message,self.result)
        speechText = ''.join(c for c in text if c not in string.punctuation)
        print(speechText)
        self.lengthoftext = len(speechText)
        print(self.lengthoftext)
        engine.say(speechText)
        engine.runAndWait()
    
    def listen(self):
        done = False
        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    
                    audio = self.recognizer.listen(mic, phrase_time_limit=5)
                    value = self.recognizer.recognize_google(audio, language='en-in')
                    value = value.lower()
                    print("value :"+ value)
                    return value
            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                self.speak("i did not understand you, please try again")
            except speech_recognition.RequestError:
                self.speak("you do not have internet access!")
            
        
    def hello(self):
        text = "hello what can i do for you sir"
        self.result = text
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        # self.speak(text)
        
        return self.result
    
    def startSplashScreen(self):
        subprocess.run(["python", "splashScreen.py"])

    def doMath(self,):
        print("DO MATH STARTED")
        # print(equation)
        self.tryWolframaalpha()
    
    def about(self):
        text = "My name is Shadow. I am an AI assistant designed to help you with various tasks"
        self.result = text
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        # self.speak(text)
        
        return self.result
        
    
    # def create_note(self):
    #     pass
    # def add_todo(self):
    #     pass
    def show_todo(self):
        print("todo")
    def quit(self):
        pid = os.getpid()  # get the process ID of the current Python script
        os.kill(pid, signal.SIGTERM)
    
    def screenshot(self):
        print("taking screenshot in 5 seconds")
        self.speak("taking screenshot in 5 seconds")
        time.sleep(5)
        winsound.PlaySound("assets/audio/shot.wav", winsound.SND_FILENAME)
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        result = "screenshot taken succesfully"
        print(result)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
    def thanks(self):
        resposnseRandom = ["You're welcome!", "Glad I could help.", "No problem!"]
        result = random.choice(resposnseRandom)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
    
    def food(self):
        resposnseRandom = ["I don't eat food","I'm a language model, so I don't have a stomach to fill with food,"]
        result = random.choice(resposnseRandom)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
    
    def marriege(self):
        resposnseRandom = ["Sorry, I don't think I'm ready for that kind of commitment","sorry i cant married","I don't have the ability to get marriege","I'm just a machine, so I don't have a heart to give away.","I am a Sigma Male"]
        result = random.choice(resposnseRandom)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
    
    def sports(self):
        resposnseRandom = ["As an AI language model, I don't have personal preferences, but many people enjoy watching and playing sports like basketball, soccer, and football.", "I don't have the ability to have a favorite team, but some popular ones include the Real Madrid, Los Angeles Lakers, and Manchester United."]
        result = random.choice(resposnseRandom)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
    def sad(self):
        resposnseRandom = ["I'm sorry to hear that. It's okay to feel sad sometimes, and it's important to take care of yourself during these times.","I'm sorry to hear that. Is there anything I can do to help you feel better?","It's okay to feel sad sometimes. I'm here to listen if you need to talk."]
        result = random.choice(resposnseRandom)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
    
    def help(self):
        resposnseRandom = ["Sure, what do you need help with?", "I'm here to help. What can I do for you?", "Let me know what you need help with."]
        result = random.choice(resposnseRandom)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
    
    def loveU(self):
        resposnseRandom = ["Aww, I appreciate your kind words!", "You're so sweet! I care about you too.", "That's very kind of you to say. I value our relationship as well."]
        result = random.choice(resposnseRandom)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
    def switch(self):
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.press("tab")
        pyautogui.keyUp("alt")
        result = "successfully switch the window"
        print(result)
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
    
    def guessWho(self):
        self.currentUser = FaceReg.startRecognitiion()
        text = 'Sorry i am not able to identify you'
        if self.currentUser == 'Dont know':
            text == "I am Sorry i dont quite recognize you!"
        elif self.currentUser == 'none found':
            text == "Sorry I am not able to identify you properly"
        else:
            text = f"Hi {self.currentUser}. How are you doing?"
        self.result = text
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
    
    def image(self):
        
        if "can you show " in self.message:
            message = self.message.split('can you show', 1)[1].strip()
        
        if "display" in self.message:
            message = self.message.split('display', 1)[1].strip()	
    
        if "show" in self.message:
            message = self.message.split('show', 1)[1].strip()

        self.get_image_from_google(message)
    
    def get_image_from_google(self,query):

        search_term = query
        if(search_term.strip()[0].isdigit()):
            search_term = search_term.split()[1:]
            search_term = ' '.join(search_term)
        
        url = "https://www.bing.com/images/search?q={}&filters=Size:Wallpaper".format(search_term)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        image_elements = soup.find_all('img', class_='mimg')
        
        image_urls = []
        for element in image_elements:
            image_url = element.get('data-src') or element.get('src')
            if image_url.startswith('http'):
                image_urls.append(image_url)
        
        if image_urls:
            print(image_urls[0])
            content = image_urls[0]
            views.Index_Avatar.test(content)
            return image_urls[0]
        else:
            print("no pic wtf")
            
    def getKeyWordsFromQuery(self,query):
        
        tokens = word_tokenize(query)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word.casefold() not in stop_words]

        # Tag the tokens with their part-of-speech
        tagged_tokens = pos_tag(tokens)

        # Filter out only the nouns and adjectives as keywords
        keywords = [word for word, pos in tagged_tokens if pos in ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS']]

        # Print the identified keywords
        return keywords
    
    def tryFromWikipedia(self,query):
        keywords = self.getKeyWordsFromQuery(query)
        seperator = ' '
        prompt = seperator.join(keywords)
        print('prompt = '+ prompt)
        
        topic = prompt
        sentences = 3
        
        try:
            summary = wikipedia.summary(topic, sentences=sentences)
            self.get_image_from_google(topic)
            self.result = summary
            threading.Thread(target=self.speak, args=(summary,)).start()
            views.Index_Avatar.promptController(self.message,self.result)
            
        except wikipedia.exceptions.PageError:
            self.default_google()
            return f"Sorry, I could not find any information on {topic}."
            
        except wikipedia.exceptions.DisambiguationError as e:
            self.default_google()
            return f"Please be more specific. It could refer to one of the following: {e.options}"
        except:
            self.default_google()
            

    
    def tryWolframaalpha(self):
        query = self.message
        appID = 'QGRJ46-GT74AUTTTW'
        client = wolframalpha.Client(appID)
        try:
            result = client.query(query)
            answer = next(result.results).text
            self.get_image_from_google(answer)
            self.result = answer
            threading.Thread(target=self.speak, args=(answer,)).start()
            views.Index_Avatar.promptController(self.message,self.result)
            
        except:
            print("not found on wolf")
            self.tryFromWikipedia(query)
    
    def default_google(self):
        
        query = self.message
        num_results = 1
        search_url = f"https://www.google.com/search?q={query}&num={num_results}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            result = soup.find("div", class_="BNeawe s3v9rd AP7Wnd").text
        except:
            print("expection in google")
        if(result):
            
            print(result)
            imageLink = self.get_image_from_google(result)
            
        else:
            result = "Sorry i cant do that yet.But i will try to improve mysef in the later updates."
            
        self.result = result
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
        
        return result
    
    def takePhoto(self):
        text = "Smile Please!"
        self.result = text
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
        cap = cv2.VideoCapture(0)
        winsound.PlaySound("assets/audio/shot.wav", winsound.SND_FILENAME)
        ret,frame = cap.read()
        cv2.imwrite('photo.jpg',frame)
        cap.release()
        remarks = ["The picture has been taken succesfully","Wow thats a good picture its a pity that the model was so ugly","The picture has been saved succesfully. What a waste of memory","Wow the picture looks better than i imagined."]
        text = random.choice(remarks)
        self.result = text
        views.Index_Avatar.promptReset()
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
    def readNews(self):
        googleNews = GoogleNews()
        timeObject = datetime.datetime.now()
        text = "what news do you want to listen to?"
        self.result = text
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        self.message = self.listen()
        
        timeAndDate = timeObject.strftime("%m/%d/%Y")
        googlenews = GoogleNews(lang='en')
        googlenews = GoogleNews(timeAndDate)
        news = googlenews.search(self.message)
        
        googlenews.result()
        result = googlenews.get_texts()
        result = result[1]
        self.result = result
        views.Index_Avatar.promptReset()
        threading.Thread(target=self.speak, args=(result,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
    
    def appstart(self):

        					#getting apps list
        print("function started for opening")
        if "open" in self.message:
            message = self.message.split('open', 1)[1].strip()
        
        if "start" in self.message:
            message = self.message.split('start', 1)[1].strip()	#removing additional commands
    
        if "run" in self.message:
            message = self.message.split('run', 1)[1].strip()
        text = "trying to open "+ message
        self.result = text
        views.Index_Avatar.promptController(self.message,self.result)
        threading.Thread(target=self.speak, args=(text,)).start()
        run(message)
        command = run("find " + message) 
        if(command):					#find if closest match is needed
            text = message + "opened succesfully"
            self.result = text
            threading.Thread(target=self.speak, args=(text,)).start()
            views.Index_Avatar.promptController(self.message,self.result)
        else:
            close = get_close_matches(message,self.appList)
            print(close)
            text = close[0] + "is the closet match do you want to open it?"
            self.result = text
            threading.Thread(target=self.speak, args=(text,)).start()
            views.Index_Avatar.promptController(self.message,self.result)
            
            confirmation = self.listen()
            print(confirmation)
            if confirmation == "yes":
                run(close[0])
        return
    def time(self):
        now = datetime.datetime.now()
        time_in_12hr_format = now.strftime("%I:%M:%S %p")
        print(time_in_12hr_format)
        text = "the time is "+ time_in_12hr_format
        self.result = text
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
    def getWeather(self):
        find = self.message

        url = f"https://www.google.com/search?q={find}"

        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        weather = soup.find("div", class_="BNeawe").text
        text = "the weather is "+weather
        self.result = text
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
    
    def writeOnScreen(self):
        text = "You can start speaking now rember to say shadow you can stop now to stop writingtext you will do"
        stopWord = "shadow stop"
        self.result = text
        #2 line for speaking and prompt
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
        while True:
            textToWrite = self.listen()
            
            if stopWord in textToWrite.lower():
                break
            else:
                pyautogui.typewrite(textToWrite)
        text = "i hope you sucessfully finished your writing.."
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(" ",text)
        
    def tellJoke(self):
        
        myJoke = pyjokes.get_joke(language='en', category='neutral')
        print(myJoke)
        self.result = myJoke
        threading.Thread(target=self.speak, args=(myJoke,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        
    def watchYoutube(self):
        
        query = self.message
        
        if "play a video" in query:
            query = query.replace("play a video","")
        if "play" in query:
            query = query.replace("play","")
        if "put on the" in query:
            query = query.replace("put on the","")
        if "can you play" in query:
            query = query.replace("can you play","")
        if "can you please" in query:
            query = query.replace("can you please","")
        if "can you" in query:
            query = query.replace("can you","")
        if "  " in query:
            query = query.replace("  "," ")
        if "in youtube" in query:
            query = query.replace("in youtube","")
        if "on youtube" in query:
            query = query.replace("on youtube","")
            
        print(f"query = {query}")
        text = f"playing {query} on youtube"
        self.result = text
        threading.Thread(target=self.speak, args=(text,)).start()
        views.Index_Avatar.promptController(self.message,self.result)
        kit.playonyt(query)
        
    def startAssistant(self):
        views.Index_Avatar.stopTalk()
        views.Index_Avatar.promptReset()
        views.Index_Avatar.resetImage()
        print("started")
        winsound.PlaySound("assets/audio/micsound.wav", winsound.SND_FILENAME)
        views.Index_Avatar.buttonClicked()
        print("started listening")
        self.message = self.listen()
        views.Index_Avatar.promptController(self.message,'...')
        print(self.message)
        views.Index_Avatar.buttonClicked()        
        try:
            self.assistant.request(self.message)
            # print("result i got" + self.result)
            # ui.promptReset()                
        except KeyError:
            print("key error")
            self.tryWolframaalpha()

def test(e):
    print("sucess")
    
def startThred(e):
  #  threading.Thread(target=voxa.startAssistant).start()
    voxa.startAssistant()
    wakeWordDetection()

def getGreeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        return "Good Morning"
    elif hour>12 and hour<18:
        return "Good afternoon"
    else:
        return "Good evening"

def greetUser():
    time.sleep(3)
    user = voxa.currentUser
    text = 'hello sir what can i do for you'
    if user == 'Dont know':
        text == "Hello Sir. I am sorry i dont recognize you!. What should i do for you today"
    elif user == 'none found':
        text == "Hello Sir. How may i Assist you today?"
    else:
        text = f"Welcome Mister {user}.How may I be of assistance to you today?"
    
    print(f"greeting = {text}")
    threading.Thread(target=voxa.speak, args=(text,)).start()
    
    
def wakeWordDetection():
    try:
        views.Index_Avatar.stopTalk()
    except:
        pass
    print("starting to listen for wake word")
    wakeWord = "shadow"
    recognizer = speech_recognition.Recognizer()
    done = False
    value = ""
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                    
                audio = recognizer.listen(mic, phrase_time_limit=5)
                value = recognizer.recognize_google(audio, language='en-in')
                value = value.lower()
                print("value :"+ value)
                
        except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
        except speech_recognition.RequestError:
                print("no internet access..")
            
        if wakeWord in value:
            done = True
            startThred("e")
            

voxa = Assistant()
threading.Thread(target=wakeWordDetection).start()
threading.Thread(target=greetUser).start()
views.Index_Avatar.micIcon.on_click = startThred

main.startGui()

