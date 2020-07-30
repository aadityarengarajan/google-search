import tkinter as tk
from tkinter import messagebox
import urllib
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr 
import pyttsx3 
import os
import time 

r = sr.Recognizer()  
engine = pyttsx3.init()



def Mbox(title, text):
    root = tk.Tk()
    root.withdraw()
    return messagebox.showinfo(title=title, message=text)


def search(q):
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    query = q
    URL = f"https://google.com/search?hl=en&q={query}"

    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)

    for i in results:
        engine.say(str(i['title']))
        engine.runAndWait()

def news():
            with sr.Microphone() as source2: 
                a=("What would you like to get news on?")
                engine.say(str(a))
                r.adjust_for_ambient_noise(source2, duration=0.2)
                while 1:
                    try:
                        audio2 = r.listen(source2)
                        MyText = r.recognize_google(audio2) 
                        break
                    except:
                        pass

                MyText = MyText.lower() 
      
                a=("Did you say "+MyText)
                engine.say(str(a))
                q=str('&tbm=nws'+str(MyText))

                while 1:
                    try:
                        audio2 = r.listen(source2)
                        MyText = r.recognize_google(audio2) 
                        break
                    except:
                        pass
                MyText = MyText.lower() 
      
                if "yes" in MyText.lower():
                    a=("Alright, giving you the top 10 results for "+q)
                    engine.say(str(a))
                    engine.runAndWait()
                    search(q)

def google():
            with sr.Microphone() as source2: 
                a=("What would you like to Google Search for?")
                engine.say(str(a))
                r.adjust_for_ambient_noise(source2, duration=0.2)
                while 1:
                    try:
                        audio2 = r.listen(source2)
                        MyText = r.recognize_google(audio2) 
                        break
                    except:
                        pass

                MyText = MyText.lower() 
      
                a=("Did you say "+MyText)
                engine.say(str(a))
                q=MyText

                while 1:
                    try:
                        audio2 = r.listen(source2)
                        MyText = r.recognize_google(audio2) 
                        break
                    except:
                        pass
                MyText = MyText.lower() 
      
                if "yes" in MyText.lower():
                    a=("Alright, giving you the top 10 results for "+q)
                    engine.say(str(a))
                    engine.runAndWait()
                    search(q)

def tdyworks():
    while 1:
        try:
            datf=open('dat.txt')
            jobs=datf.readlines()
            datf.close()
            a=("Here are the works to be done today")
            engine.say(str(a))
            engine.runAndWait()
            for i in jobs:
                engine.say(str(i))
                engine.runAndWait()
                time.sleep(0.1)
            Mbox('Todays Works', str(jobs))
            os.remove('dat.txt')
            break
        except:
            pass

def wikipedia(q):

    res = requests.get('https://en.wikipedia.org/wiki/' + q)

    res.raise_for_status()
    wiki = bs4.BeautifulSoup(res.text,"lxml")
    elems = wiki.select('p')
    for i in range(len(elems)):
        engine.say((elems[i].getText())[:150])
        engine.runAndWait()

def youtube(q):
    textToSearch = q
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        return ('https://www.youtube.com' + vid['href'])

while(1):     
    try:
        a=("Greetings! And Welcome back!")
        engine.say(str(a))
        engine.runAndWait()
        with sr.Microphone() as source2: 
                r.adjust_for_ambient_noise(source2, duration=0.2)
                while 1:
                    try:
                        a=("Waiting for input")
                        engine.say(str(a))
                        engine.runAndWait()
                        audio2 = r.listen(source2)
                        MyText = r.recognize_google(audio2) 
                        break
                    except:
                        pass

                MyText = MyText.lower() 
      
                a=("Did you say "+MyText)
                engine.say(str(a))
                q=MyText

                while 1:
                    try:
                        audio2 = r.listen(source2)
                        MyText = r.recognize_google(audio2) 
                        break
                    except:
                        pass
                MyText = MyText.lower() 
      
                if "yes" in MyText.lower():
                    if "news" in q.lower():
                        q=q.replace('news','')
                        news()
                    elif "search" in q.lower():
                        q=q.replace('search','')
                        search(q)
                    elif "google" in q.lower():
                        q=q.replace('google','')
                        google()
                    elif "wikipedia" in q.lower():
                        q=q.replace('wikipedia','')
                        wikipedia(q)
                    elif "define" in q.lower():
                        q=q.replace('define','')
                        google()
                    elif "what is" in q.lower():
                        q=q.replace('what is','')
                        search(q)
                    elif "you tube" in q.lower():
                        q=q.replace('you tube','')
                        webbrowser.open_new_tab(youtube(q))
                    elif "youtube" in q.lower():
                        q=q.replace('youtube','')
                        webbrowser.open_new_tab(youtube(q))
                    elif "open" in q.lower():
                        q=q.replace('open','')
                        webbrowser.open_new_tab(q.lower())

    except:
        print(z)

