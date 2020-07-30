import tkinter as tk
from tkinter import messagebox
import urllib
import requests
from bs4 import BeautifulSoup
import os
import time
import webbrowser
#from newspaper import news

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
    c=0
    for i in results:
        c+=1
        print(c,str(i['title']))
    opin=int(input('OPEN : '))
    try:
        print(c-1,results[opin-1],results[opin-1]['link'])
        webbrowser.open_new_tab(results[opin-1]['link'])
    except Exception as e:
        print(e)

def wikipedia(q):
    res = requests.get('https://en.wikipedia.org/wiki/' + q)
    res.raise_for_status()
    wiki = BeautifulSoup(res.text,"lxml")
    elems = wiki.select('p')
    for i in range(2):
        print((elems[i].getText())) 


while 1:
    q=input("INPUT : ")
    if "news" in q.lower():
        q=q.replace('news','')
        news(q)
    elif "search" in q.lower():
        q=q.replace('search','')
        search(q)
    elif "google" in q.lower():
        q=q.replace('google','')
        search(q)
    elif "wikipedia" in q.lower():
        q=q.replace('wikipedia','')
        wikipedia(q)
    elif "define" in q.lower():
        q=q.replace('define','')
        search(q)
    elif "what is" in q.lower():
        q=q.replace('what is','')
        search(q)
    elif "open" in q.lower():
        q=q.replace('open','')
        webbrowser.open_new_tab(q.lower())
