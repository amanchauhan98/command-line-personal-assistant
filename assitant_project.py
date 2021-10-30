# from _typeshed import OpenTextMode
from importlib import import_module
import webbrowser
import os
import speedtest
from win32api import SearchPath
from win32com.client import build, util
import json
import phonenumbers
from phonenumbers import carrier , geocoder, timezone
import re
import pyqrcode
from captcha.image import ImageCaptcha
import png
from pyqrcode import QRCode
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import folium
from googlesearch import search
from GoogleNews import GoogleNews
from gtts import gTTS
import pywhatkit as kit
from pygame import mixer
from instabot import Bot

# def music(file):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     # time.sleep(20)

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def news():
    googlenews = GoogleNews()
    googlenews = GoogleNews(period='7d')
    googlenews.search('IN')
    reuslt = googlenews.result()
    for x in reuslt:
        print("-"*50)
        print("title--",x['title'])  
        speak(x['title']) 
        print("datetime--",x['date'])
        print("descroption--",x['desc'])
        speak(x['desc'])
        print("link--",x['link']) 

def whatsupp():
    print("enter the phone number")
    speak("enter the phone number")
    number = input()
    print("enter the message which you want to send")
    speak("enter the message which you want to send")
    message = input()
    kit.sendwhatmsg(f"+91 {number}",f"{message}",16,33)

def google():
    print("enter your querry here")
    speak("enter your querry here")
    querry = input()
    for i in search(querry, num=10,stop = 10, pause=1, ) :
        speak("here is your result...")
        print(i)
    speak("done, aman chauhan")

def maps():
    # print("enter the location here")
    # speak("enter the location here")
    # m = input()
    map1 = folium.Map(location=[28.3648217,77.2749958], zoom_start=16)
    map1.save("index.html")
    webbrowser.open("index.html")
    speak("here is your result aman chauhan")
def drive() :
    print("Enter the path here")
    speak("enter the path here")
    path = input(r"")

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)
    for x in os. listdir(path) :
        f = drive.CreateFile({'title': x})
        f.SetContentFile(os.path.join(path,x))
        f.Upload()
        f = None
    speak("done mr. aman chauhan") 

def upload_insta():
    bot = Bot()
    bot.login(username = "lets__study__c__program__", password = "fuck123*")
    bot.upload_photo("11.jpg",caption= "This is just a deleted picture")

def phone_details():
    mobileno = input("Enter the Mobile number with country code\n")
    mobileno = phonenumbers.parse(mobileno)

    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "en"))
    print(geocoder.description_for_number(mobileno, "en"))
    print("validate mobile no :", phonenumbers.is_valid_number(mobileno))
    print("checking possibility of number :", phonenumbers.is_possible_number(mobileno))

def QRcode() :
    s = input("Enter the link here for generate your QR code\n")
    file = input("enter the image name\n")
    url = pyqrcode.create(s)
    url.svg(f"{file}.svg", scale=8)
    url.png(f"{file}.png", scale=6)

def generate_captcha() :
    image = ImageCaptcha(width=280, height=91)
    captcha_text = input("enter the text for getting in captcha\n")
    image = input("Enter the image name\n")
    data = image.generate(captcha_text)
    image.write(captcha_text,"captchatr.png")


def extract_email():
    myText = """
    They are our Developers
They helped each other and Build this Organisation.

NAME	TITLE	STATUS	ROLE	Edit

Aman Chauhan
avinashthakurchauhan07@gmail.com
Front End developer
Customize the UI/UX
Active	Admin

Deepak Giri
deepak.giri@acem.edu.in
Back End developer
Customize Database
Active	Admin

Kunal Singhal
kunal.singhal@acem.edu.in
Content Writer
Updating version and Content
Active	Admin

Vishal Keshri
vishal.keshri@acem.edu.in
Manages Websites Traffic
Control Over Website
Active	Admin	Edit

    """
    mail = re.findall(r"[A-Za-z0-9*-_&%]+@[A-Za-z0-9*-_&%]+.[A-Za-z1-9]+",myText)
    for i in mail:
        print(i)




    


def calculator():
    speak("enter the 1st number")
    num1 = input("enter the 1st number \n")
    speak("enter the 2st number")
    num2 = input("enter the 2nd number\n")
    speak("enter the operator")
    op = input("enter the operator\n")
    
    if op == "+" :
        print(f"the sum of two number is {num1+num2}")
    elif op == "-" :
        print(f"the difference between two number is {num1 - num2}")    
    elif op == "*" :
        print(f"the product of two number is {num1 * num2}")
    elif op == "/" :
        print(f"the divison of two number is {num1/num2}")
    elif op == "%" :
        print(f"the modulas of two number is {num1 % num2}")
    elif op.isnumeric():
        raise Exception("you entered the wrong the input in operator.")
        




def pythontut():
    pass

if __name__ == '__main__':
    print("|_______________________|")
    print("    ASSITANT PROJECT      ")
    print("|_______________________|")
    with open("assistant_intro.txt","r") as f :
        speak(f.read())
    enter = input("Enter the input here\n") 
    speak("just wait a second!")
    while True:
        if enter == "open file":
            file = input("enter the name of file\n")
            a = os.system(file)
            print(a)   
            speak(f"hey, there is your {file}") 
            break
        
        elif enter == "open browser":
            speak("just  wait a second !")
            webbrowser.Chrome.open("www.google.com")
            webbrowser.Chrome.open_new_tab("www.google.com")
            speak(f"hey, there is your result")
            break

        elif enter == "make folder" :
            print("enter the name of folder you want to get!")
            speak("enter the name of folder you want to get!")
            folder = input()
            speak("just  wait a second !")
            os.mkdir(folder)
            print("done,aman chauhan")
            speak("done,aman chauhan")
            break

        elif enter == "make file":
            print("enter the name of file which you want to get!")
            speak("enter the name of file which you want to get!")
        
            ask_file = input()
            speak("just  wait a second !")
            with open(ask_file,"a") as h:
                print("write here in your file")
                speak("write here in your file")
                h.write(input())
                h = open(ask_file)
            print(f"your {ask_file} path is {os.getcwd()}")
            speak(f"your {ask_file} path is {os.getcwd()}")
            speak("done Mr. aman chauhan")
            break
        elif enter == "play music":
            print("wait a second")
            speak("wait a second")
            import Music_player
            print(Music_player)
            break
        elif enter == "get news":
            # print("which country do you want to get news")
            # speak("which country do you want to get news")
            # country = input()
            print("wait a second")
            speak("wait a second")
            news()
            speak("here is your news aman chauhan")
            break
        elif enter == "send message":
            print("wait a second")
            speak("wait a second")
            whatsupp()
            speak("done aman chauhan, please click on send and deliever your message.")
            break
        elif enter == "google search" :
            print("wait a second")
            speak("wait a second")
            google()
            break
        elif enter == "open map" :
             print("wait a second")
             speak("wait a second")
             maps()
             break
        elif enter == "upload files" :
            print("wait a second")
            speak("wait a second")
            drive()
            break
        elif enter == "play games":
             print("wait a second")
             speak("wait a second")
             print("which game do you want to play? like Stone paper scissor , Odd even prime game and snake water gun?")
             speak("which game do you want to play? like Stone paper scissor , Odd even prime game and snake water gun?")
             
             game = input()
             if game == "stone paper scissor" :
                 print("Loading, Please wait")
                 speak("Loading, Please wait")
                 import stone_paper_scissor_game
                 print(stone_paper_scissor_game)
                 print("thank you")
                 speak("thank you for playing")
             elif game == "snake water gun" :
                print("Loading, Please wait")
                speak("Loading, Please wait")
                import snake_water_gun
                print(snake_water_gun)
                print("thank you")
                speak("thank you for playing")
             elif game == "odd even prime" :
                print("Loading, Please wait")
                speak("Loading, Please wait")
                import odd_even_prime_game
                print(odd_even_prime_game)
                print("thank you")
                speak("thank you for playing")   
             else :
                 print("ERROR!!!")
                 speak("sorry! you enterd the wrong input. please try again") 
             break

        elif enter == "upload photo in insta":
            print("Loading, Please wait")
            speak("Loading, Please wait")
            upload_insta()
            print("done Mr. aman chauhan")
            speak("the photo was uploaded aman chauhan")
            break
        elif enter == "calculator":
            print("Loading, Please wait")
            speak("Loading, Please wait")
            calculator()
            break
        elif enter == "extract email" :
            print("Loading, Please wait")
            speak("Loading, Please wait")
            extract_email()
            break
        elif enter == "show database" :
            print("Loading, Please wait")
            speak("Loading, Please wait")
            import mysqllib
            print(mysqllib)
            speak("here is your SQL Library")
            break
        elif enter == "open dictionary" :
            print("Loading, Please wait")
            speak("Loading, Please wait")
            import dictionary_app_GUI
            speak("Here is your result aman chauhan")
            print(dictionary_app_GUI)
            break
        
        elif enter == "phone details" :
            print("Loading, Please wait")
            speak("Loading, Please wait")
            phone_details()
            speak("Here is your result aman chauhan")
            break
        elif enter == "generate QR code" :
            print("Loading, Please wait")
            speak("Loading, Please wait")
            QRcode()
            speak("Here is your result aman chauhan")
            break
        elif enter == "generate captcha" :
            print("Loading, Please wait")
            speak("Loading, Please wait")
            generate_captcha()
            speak("Here is your result aman chauhan")
            break
        elif enter == "youtube downloader" :
            print("Loading, Please wait")
            speak("Loading, Please wait")
            import youtube_video_downloder
            print(youtube_video_downloder)
            speak("Here is your result aman chauhan")
            break












             



                   









            
            




            






            



            








