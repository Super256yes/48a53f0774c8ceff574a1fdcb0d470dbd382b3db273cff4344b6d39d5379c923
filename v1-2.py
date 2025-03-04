import time #line:1
import os #line:2
import subprocess #line:3
import keyboard #line:4
import pyautogui #line:5
from datetime import datetime #line:6
from PIL import Image #line:7
import pytesseract #line:8
from pytesseract import image_to_string #line:9
import requests #line:10
import json #line:11
from gtts import gTTS #line:12
from groq import Groq #line:13
from screeninfo import get_monitors #line:14
from openai import OpenAI #line:15
import base64 #line:16
from colorama import Fore #line:17
import hashlib #line:18
import colorama #line:19
import socket #line:20
import sys #line:21
import tkinter as tk #line:22
from tkinter import font #line:23
import os #line:24
import json #line:25
import ctypes #line:26
import time #line:27
import screeninfo #line:28
from pynput import keyboard as kb #line:29
import pyautogui #line:30
clientName ="theArc"#line:33
version ="v1.2"#line:34
buildDate ="March 3th, 2025"#line:35
vlc_path ="vlc.exe"#line:36
inputCheckDelay =0.016666 #line:37
hostname =socket .gethostname ()#line:38
ip_address =socket .gethostbyname (hostname )#line:39
skipKeyCheck =""#line:40
clientKey =""#line:41
colorama .init ()#line:43
if __name__ =="__main__":#line:45
    if len (sys .argv )>1 :#line:46
        skipKeyCheck =sys .argv [1 ]#line:47
    else :#line:48
        skipKeyCheck =""#line:49
    print ("skipKeyCheck:",skipKeyCheck )#line:51
headers ={'Content-Type':'application/json'}#line:55
def toSHA256 (O00O000O0OOOOO0O0 ):#line:57
    O000O0O000000000O =hashlib .sha256 ()#line:58
    O000O0O000000000O .update (O00O000O0OOOOO0O0 .encode ('utf-8'))#line:59
    OO0OOOO0OOO0O0OO0 =O000O0O000000000O .hexdigest ()#line:60
    return OO0OOOO0OOO0O0OO0 #line:61
def getLocalIP ():#line:63
    O00O0OO00OOOO000O =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )#line:64
    try :#line:65
        O00O0OO00OOOO000O .connect (("8.8.8.8",80 ))#line:67
        OOOOOOO0OOO00000O =O00O0OO00OOOO000O .getsockname ()[0 ]#line:68
    except Exception as O00OO000O000O0O0O :#line:69
        OOOOOOO0OOO00000O ="Unable to get local IP"#line:70
    finally :#line:71
        O00O0OO00OOOO000O .close ()#line:72
    return OOOOOOO0OOO00000O #line:73
def log (OOO00O00O0O0O000O ):#line:75
    print (f"[{Fore.GREEN}INFO{Fore.RESET}] {OOO00O00O0O0O000O}")#line:76
def logError (O0OO000O0O0OO000O ):#line:78
    print (f"[{Fore.RED}ERROR{Fore.WHITE}] {O0OO000O0O0OO000O}")#line:79
def logWarning (OO0OO0O0O0O000OOO ):#line:81
    print (f"[{Fore.YELLOW}WARNING{Fore.WHITE}] {OO0OO0O0O0O000OOO}")#line:82
def logFatal (OO00OOOOO0O00OOO0 ):#line:84
    print (f"[{Fore.RED}FATAL{Fore.WHITE}] {OO00OOOOO0O00OOO0}. theArc will automatically close in 10 seconds.")#line:85
    time .sleep (10 )#line:86
    exit ()#line:87
def pingDomain (OOO00000OO00OO0OO ,OO0O0O0OO0O000O0O ):#line:89
    try :#line:90
        O00000O00OOOOO000 =requests .get (f"http://{OOO00000OO00OO0OO}",timeout =5 )#line:91
        if O00000O00OOOOO000 .status_code ==200 :#line:92
            if OO0O0O0OO0O000O0O ==True :#line:93
                log (f"Website: {OOO00000OO00OO0OO} Status:"+Fore .GREEN +" Connected"+Fore .RESET +f" - Status Code: {O00000O00OOOOO000.status_code}")#line:94
            return True #line:95
        else :#line:96
            if (O00000O00OOOOO000 .status_code ==403 ):#line:97
                    if OO0O0O0OO0O000O0O ==True :#line:98
                        log (f"Website: {OOO00000OO00OO0OO} Status:"+Fore .GREEN +" Connected"+Fore .RESET +f" - Status Code: {O00000O00OOOOO000.status_code}")#line:99
                    return True #line:100
            else :#line:101
                if OO0O0O0OO0O000O0O ==True :#line:102
                    logError (f"Website: {OOO00000OO00OO0OO} Status:"+Fore .RED +f" Unable to Connect (Status code: {O00000O00OOOOO000.status_code})"+Fore .RESET )#line:103
                return False #line:104
    except requests .exceptions .RequestException as O000OO0OO00OOOO0O :#line:105
        if OO0O0O0OO0O000O0O ==True :#line:106
            logError (f"Website: {OOO00000OO00OO0OO} Status:"+Fore .RED +" Unable to Connect"+Fore .RESET )#line:107
        return False #line:108
def logThroughWebhook (O0O00O00OO00OOOO0 ):#line:110
    OO000O0O0O0O0O0OO ={'content':'{}'.format (O0O00O00OO00OOOO0 ),'username':'theArc'}#line:115
    requests .post ("https://discord.com/api/webhooks/1336862514591305810/O4YZZalX6AJXut4TEY0_4EEXb13eEmu6C4v3MKCzHLROATyfkdxyt-wzWWI14vV9WutT",data =json .dumps (OO000O0O0O0O0O0OO ),headers =headers )#line:116
os .system ("cls")#line:118
if pingDomain ("raw.githubusercontent.com",False )==False :#line:119
    logFatal ("Was unable to connect to 'raw.githubuser.content.com' which is required to run to program. Make sure that it isn't being blocked by a firewall.")#line:120
def get_text_from_github_raw (OO0O000OO000OOOOO ):#line:128
    OO00OO0O000OOO0O0 =requests .get (OO0O000OO000OOOOO )#line:129
    if OO00OO0O000OOO0O0 .status_code ==200 :#line:130
        O00O00O0O00000OOO =OO00OO0O000OOO0O0 .text #line:131
        OOOOOO00OOO00OO0O =O00O00O0O00000OOO .split ('\n')#line:132
        return OOOOOO00OOO00OO0O #line:133
    else :#line:134
        print ("Failed to fetch the text from the given URL.")#line:135
        return []#line:136
raw_url ='https://raw.githubusercontent.com/Super256yes/48a53f0774c8ceff574a1fdcb0d470dbd382b3db273cff4344b6d39d5379c923/refs/heads/super/48a53f0774c8ceff574a1fdcb0d470dbd382b3db273cff4344b6d39d5379c923.txt'#line:139
listOfKeys =get_text_from_github_raw (raw_url )#line:140
doLogging =False #line:143
if pingDomain ("discord.com/api/webhooks/1336862514591305810/O4YZZalX6AJXut4TEY0_4EEXb13eEmu6C4v3MKCzHLROATyfkdxyt-wzWWI14vV9WutT",False )==True :#line:144
    doLogging =True #line:145
configJsonFile =open ("config.json","r",encoding ="utf-8")#line:153
configJsonFileData =json .load (configJsonFile )#line:154
configJsonFile .close ()#line:155
clientKey =configJsonFileData ["client_key"]#line:157
if skipKeyCheck !="skipKeyCheck":#line:159
    for x in range (len (listOfKeys )):#line:160
        if toSHA256 (clientKey )==listOfKeys [x ]:#line:161
            log ("Key has been successfully validated.")#line:162
            log ("Welcome user ID: "+str (x ))#line:163
            if doLogging ==True :#line:164
                logThroughWebhook (f"VALID KEY LOGIN:\nKey: {clientKey} \nIP Adress: {ip_address} \nHost Name: {hostname}\nNetwork Address: {getLocalIP()}")#line:165
            break #line:166
        else :#line:167
            if x +1 ==len (listOfKeys ):#line:168
                logThroughWebhook (f"INVALID KEY LOGIN:\nAttempted Key: {clientKey} \nIP Adress: {ip_address} \nHost Name: {hostname}\nNetwork Address: {getLocalIP()}")#line:169
                logFatal ("Key is invalid. Make sure you properly put your key into the parameter 'client_key' in 'config.json'.")#line:170
    pressEnter =input ("[{}]: Press 'Enter' to start the program.".format (clientName ))#line:174
    log ("Attempting to start program...")#line:175
    os .system ("cls")#line:177
else :#line:178
    logWarning ("skipped the checking of the key")#line:179
print (Fore .LIGHTRED_EX +"""


        ▄▄▄█████▓ ██░ ██ ▓█████ ▄▄▄       ██▀███   ▄████▄  
        ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  
        ▒ ▓██░ ▒░▒██▀▀██░▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ 
        ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒
          ▒██▒ ░ ░▓█▒░██▓░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░
          ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░
            ░     ▒ ░▒░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒   
          ░       ░  ░░ ░   ░    ░   ▒     ░░   ░ ░        
                  ░  ░  ░   ░  ░     ░  ░   ░     ░ ░      
                    developed by: wassaps         ░        
                    
      """+Fore .RESET )#line:196
log ("Program is starting. {}, {} developed by wassaps.".format (clientName ,version ))#line:198
configJsonFile =open ("config.json","r",encoding ="utf-8")#line:200
configJsonFileData =json .load (configJsonFile )#line:201
configJsonFile .close ()#line:202
log ("config data has been sucessfully loaded from 'config.json'")#line:204
groq_api_key =configJsonFileData ["groq_api_key"]#line:206
log ("Set groq api key to: {}".format (groq_api_key ))#line:207
webhook_url =configJsonFileData ["webhook_url"]#line:208
log ("Set webhook url to: {}".format (webhook_url ))#line:209
discord_user_id =configJsonFileData ["discord_user_id"]#line:210
log ("Set discord user id to: {}".format (discord_user_id ))#line:211
delete_cache_option =configJsonFileData ["delete_cache"]#line:212
log ("Set'delete_cache_option' to: {}".format (delete_cache_option ))#line:213
read_response_sound =configJsonFileData ["read_response_sound"]#line:214
log ("Set'read_response_sound' to: {}".format (read_response_sound ))#line:215
discord_webhook_enabled =configJsonFileData ["discord_webhook_enabled"]#line:216
log ("Set'discord_webhook_enabled' to: {}".format (discord_webhook_enabled ))#line:217
show_response_text =configJsonFileData ["show_response_text"]#line:218
log ("Set'show_response_text' to: {}".format (show_response_text ))#line:219
allow_image_sending =configJsonFileData ["allow_image_sending"]#line:220
log ("Set'allow_image_sending' to: {}".format (allow_image_sending ))#line:221
openai_api_key =configJsonFileData ["openai_api_key"]#line:222
log ("Set'openai_api_key' to: {}".format (openai_api_key ))#line:223
override_groq_with_chatgpt =configJsonFileData ["override_groq_with_chatgpt"]#line:224
log ("Set'override_groq_with_chatgpt' to: {}".format (override_groq_with_chatgpt ))#line:225
allow_text_input =configJsonFileData ["allow_text_input"]#line:226
log ("Set'allow_text_input' to: {}".format (allow_text_input ))#line:227
log ("all enviroment variables have been sucessfully set based on config.json")#line:229
pingDomain ("raw.githubusercontent.com",True )#line:233
if pingDomain ("discord.com",True )==False :#line:235
    if discord_webhook_enabled ==True :#line:236
        logFatal ("Could not connect to 'discord.com' while being required within 'config.json'")#line:237
    else :#line:238
        logWarning ("Could not connect to 'discord.com' but will ignore it since it isnt required based on the config.")#line:239
if pingDomain ("chatgpt.com",True )==False :#line:241
    if override_groq_with_chatgpt or allow_image_sending ==True :#line:242
        logFatal ("Could not connect to 'chatgpt.com' while being required within 'config.json'")#line:243
    else :#line:244
        logWarning ("Could not connect to 'chatgpt.com' but will ignore it since it isnt required based on the config.")#line:245
if pingDomain ("groq.com",True )==False :#line:247
    if override_groq_with_chatgpt ==False :#line:248
        logFatal ("Could not connect to 'groq.com' while being required within 'config.json'")#line:249
    else :#line:250
        logWarning ("Could not connect to 'groq.com' but will ignore it since it isnt required based on the config.")#line:251
if (read_response_sound ==True ):#line:255
    log ("testing audio playback for driver issues")#line:256
    time .sleep (.5 )#line:257
    subprocess .run ([vlc_path ,'--intf','dummy','--no-video','--play-and-exit','audioPlaybackTestAudio.mp3'])#line:258
    log ("launching threadingBypass.py")#line:259
    time .sleep (.5 )#line:260
    subprocess .Popen (['start','cmd','/k',f'python {"threadingBypass.py"}'],shell =True )#line:261
    log ("threadingBypass.py was launched")#line:262
    time .sleep (.5 )#line:263
else :#line:264
    log ("Skipping audio playback test since 'read_response_sound' has been set to False.")#line:265
    log ("skipped the opening of threadingBypass.py since it wasn't needed based on the current config.")#line:266
monitor =get_monitors ()[0 ]#line:268
sizeOfScreenForX =monitor .width #line:269
sizeOfScreenForY =monitor .height #line:270
log ("detected resolution as primary display as {}x{}".format (sizeOfScreenForX ,sizeOfScreenForY ))#line:272
if override_groq_with_chatgpt ==False :#line:274
    groqClient =Groq (api_key =groq_api_key ,)#line:278
    log ("groq api key initialized")#line:280
else :#line:281
    log ("skipped initialization of groq_api key since 'override_groq_with_chatgpt' is set to True.")#line:282
if override_groq_with_chatgpt ==True or allow_image_sending ==True :#line:284
    openAIClient =OpenAI (api_key =openai_api_key )#line:285
    log ("OpenAI key initialized")#line:286
pytesseract .pytesseract .tesseract_cmd ="tesseract.exe"#line:295
log ("tesseract.exe initialized")#line:297
def extract_text_from_image (OO0000000O0OO0000 ):#line:299
    with Image .open (OO0000000O0OO0000 )as O000000O000OOO00O :#line:300
        OO0O0O0OOO0OOO0O0 =pytesseract .image_to_string (O000000O000OOO00O )#line:301
    return OO0O0O0OOO0OOO0O0 #line:302
def take_screenshot ():#line:304
    O0O0000OO0O0O00OO =datetime .now ()#line:305
    O0O000OOO000OO0OO =O0O0000OO0O0O00OO .strftime ("%Y%m%d_%H%M%S")+".png"#line:306
    O00O00OO0O00O00O0 =pyautogui .screenshot ()#line:307
    OOO0O00O00OOOO0O0 ="cache"#line:309
    if not os .path .exists (OOO0O00O00OOOO0O0 ):#line:310
        os .makedirs (OOO0O00O00OOOO0O0 )#line:311
        log ("Created missing directory /cache/.")#line:312
    OO0O00OO0OO0000OO =os .path .join (OOO0O00O00OOOO0O0 ,O0O000OOO000OO0OO )#line:314
    O00O00OO0O00O00O0 .save (OO0O00OO0OO0000OO )#line:315
    log ("Screenshot saved at: {}".format (OO0O00OO0OO0000OO ))#line:316
    return OO0O00OO0OO0000OO #line:317
def sendResponseThroughWebhook (OOOOO0OOO0OO00O00 ):#line:319
    OO00O000OO000OO00 ={'content':'<@{}> {}'.format (discord_user_id ,OOOOO0OOO0OO00O00 ),'username':clientName }#line:324
    O000OO000000000O0 =requests .post (webhook_url ,data =json .dumps (OO00O000OO000OO00 ),headers =headers )#line:325
    if O000OO000000000O0 .status_code ==204 :#line:326
        log ('Answer send to webhook sucessfully')#line:327
    else :#line:328
        logWarning ('Failed to sent answer to webhook')#line:329
def sendResponseThroughWindow (OOOOOOO0OOO000000 ):#line:331
    if hasattr (OOOOOOO0OOO000000 ,'message')and hasattr (OOOOOOO0OOO000000 .message ,'content'):#line:333
        O0000O00OOO0O00O0 =OOOOOOO0OOO000000 .message .content #line:334
    else :#line:335
        O0000O00OOO0O00O0 =str (OOOOOOO0OOO000000 )#line:336
    with open ("transferer.json","r",encoding ="utf-8")as O0OO0O0O0OO0OOOOO :#line:337
        O000OO0OOOOOO00OO =json .load (O0OO0O0O0OO0OOOOO )#line:338
        log ("JSON data has been successfully read.")#line:339
        O000OO0OOOOOO00OO ["aiResponse"]=O0000O00OOO0O00O0 #line:340
        log ("Updated aiResponse to '{}'.".format (O0000O00OOO0O00O0 ))#line:341
        with open ("transferer.json","w",encoding ="utf-8")as O0OO0O0O0OO0OOOOO :#line:342
            json .dump (O000OO0OOOOOO00OO ,O0OO0O0O0OO0OOOOO ,indent =4 ,ensure_ascii =False )#line:343
        log ("wrote aiResponse to file.")#line:344
        log ("opening textViewer.pyw.")#line:345
        os .system ("textViewer.pyw")#line:346
        log ("textViewer.pyw closed.")#line:347
def readResponse (OO00O0OO0O00O00OO ):#line:349
    log ('Trying to read ')#line:351
    OO0000OOO0O00O0O0 ='en'#line:352
    OOO00O0OOOO0OOOOO =gTTS (text =OO00O0OO0O00O00OO ,lang =OO0000OOO0O00O0O0 ,slow =False )#line:353
    OOO00O0OOOO0OOOOO .save ("audio.mp3")#line:354
    subprocess .run ([vlc_path ,'--intf','dummy','--no-video','--play-and-exit','audio.mp3'])#line:355
    log ("Playing 'audio.mp3' from cache!")#line:356
    os .system ("del audio.mp3")#line:357
def takeScreenshot ():#line:359
    O0O0O0O000OO0O00O =take_screenshot ()#line:360
    log ("Screenshot Captured.")#line:361
    log ("Path to screenshot: "+O0O0O0O000OO0O00O )#line:362
    return O0O0O0O000OO0O00O #line:363
def encode_image (OOO00000OO00O0OOO ):#line:365
    with open (OOO00000OO00O0OOO ,"rb")as OOO00OOOOO0OOO0OO :#line:366
        return base64 .b64encode (OOO00OOOOO0OOO0OO .read ()).decode ("utf-8")#line:367
log ("methods initialized")#line:369
print ("""

░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░     {} {}
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░     Made by: wassaps
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█     “In the real world, cheaters get ahead.”
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░     
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░     
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░     
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░     
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░     
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░   
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░

""".format (clientName ,version ))#line:389
log ("{} started! Press ALT+H to show list of keybinds.".format (clientName ))#line:390
while True :#line:392
    time .sleep (inputCheckDelay )#line:394
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('T'):#line:396
        time .sleep (.5 )#line:397
        log ("Terminating Program")#line:398
        os .system ("cls")#line:399
        exit ()#line:400
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('C'):#line:402
        log ("Clearing output.")#line:403
        os .system ("cls")#line:404
        time .sleep (.5 )#line:405
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('H'):#line:407
        print ("""\nLIST OF KEYBINDS:
ALT+GRAVE(`) -> captures screenshot extracts text and sends text to AI
ALT+SHIFT+GRAVE(`) -> captures screenshot and directly sends it to AI
ALT+1 -> opens text input and allows you to directly ask the preferred AI questions.
ALT+T -> Terminates Program and threading windows
ALT+H -> shows list of keybinds
ALT+I -> shows program info
ALT+C -> clears console output""")#line:415
        time .sleep (.5 )#line:416
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('I'):#line:418
        print ("""\n{}
Developed by: wassaps
Version: {}
Build Released on: {}""".format (clientName ,version ,buildDate ))#line:422
        time .sleep (.5 )#line:423
    if keyboard .is_pressed ("Alt")and keyboard .is_pressed ("1"):#line:425
        log ("Opening text input")#line:426
        global user_input #line:427
        user_input =""#line:428
        enter_pressed =False #line:429
        def close_window ():#line:431
            global enter_pressed #line:432
            enter_pressed =True #line:433
            root .after (0 ,lambda :(root .quit (),root .destroy ()))#line:435
        def update_text_display ():#line:437
            label .config (text =user_input +"\n\n\n\n\nPRESS ENTER TO CLOSE WINDOW")#line:438
        root =tk .Tk ()#line:440
        root .overrideredirect (True )#line:443
        root .attributes ("-topmost",True )#line:446
        root .attributes ("-alpha",0.8 )#line:447
        root .geometry ("{}x{}+{}+{}".format (int (sizeOfScreenForX *.885 ),int (sizeOfScreenForY *.277 ),int (sizeOfScreenForX /19.2 ),int (sizeOfScreenForY /4 )))#line:450
        frame =tk .Frame (root ,bg ="#333333",bd =5 )#line:452
        frame .pack (expand =True ,fill =tk .BOTH )#line:453
        text_frame =tk .Frame (frame ,bg ="#333333")#line:455
        text_frame .pack (fill =tk .BOTH ,expand =True )#line:456
        custom_font =font .Font (family ="Arial",size =12 ,weight ="bold")#line:458
        label =tk .Label (text_frame ,text ="",font =custom_font ,bg ="#333333",fg ="white",justify ="left",anchor ="center",wraplength =1650 )#line:459
        label .pack (side =tk .TOP ,anchor ="center",padx =10 ,pady =10 )#line:460
        root .withdraw ()#line:462
        root .after (10 ,lambda :root .deiconify ())#line:463
        def on_press (OO0OO00O0OO00OOO0 ):#line:465
            global user_input ,enter_pressed #line:466
            if enter_pressed :#line:467
                return False #line:468
            try :#line:470
                if hasattr (OO0OO00O0OO00OOO0 ,'char')and OO0OO00O0OO00OOO0 .char is not None :#line:471
                    user_input +=OO0OO00O0OO00OOO0 .char #line:472
                elif OO0OO00O0OO00OOO0 ==kb .Key .space :#line:473
                    user_input +=" "#line:474
                elif OO0OO00O0OO00OOO0 ==kb .Key .backspace :#line:475
                    user_input =user_input [:-1 ]#line:476
                elif OO0OO00O0OO00OOO0 ==kb .Key .enter :#line:477
                    close_window ()#line:478
                    return False #line:479
                update_text_display ()#line:481
            except AttributeError :#line:482
                pass #line:483
        listener =kb .Listener (on_press =on_press )#line:485
        listener .start ()#line:486
        root .mainloop ()#line:488
        listener .stop ()#line:490
        log (f"User wrote {user_input} inside of the window")#line:492
        if (override_groq_with_chatgpt !=True ):#line:495
            log ('Using groq api to get response.')#line:496
            response =groqClient .chat .completions .create (messages =[{"role":"user","content":user_input }],model ="llama3-8b-8192",)#line:505
            aiResponse =response .choices [0 ].message .content #line:507
        else :#line:508
            log ('Using ChatGPT to get response.')#line:509
            completion =openAIClient .chat .completions .create (model ="gpt-4o",messages =[{"role":"user","content":"Do not format the response. act like you can read this in a txt."+user_input }])#line:516
            aiResponse =completion .choices [0 ].message .content #line:517
        log (aiResponse )#line:518
        if (show_response_text ==True ):#line:520
            sendResponseThroughWindow (aiResponse )#line:521
        if (discord_webhook_enabled ==True ):#line:523
            sendResponseThroughWebhook (aiResponse )#line:524
        if (read_response_sound ==True ):#line:526
            readResponse (aiResponse )#line:527
        log ('Procedure complete. Press ALT+H to show a list of keybinds.')#line:529
    if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('Shift')and keyboard .is_pressed ('`'):#line:535
        if allow_image_sending ==True :#line:537
            log ("Using screenshot to send to ai")#line:538
            image_path =takeScreenshot ()#line:539
            base64_image =encode_image (image_path )#line:541
            log ("You are now about the witness the strength of street knowledge. (if the api shit works)")#line:543
            response =openAIClient .chat .completions .create (model ="gpt-4o-mini",messages =[{"role":"user","content":[{"type":"text","text":"I want you to interperet the question/prompt/image which is asked in this photo. Do not format the response. act like you can read this in a txt.",},{"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{base64_image}"},},],}],)#line:562
            aiResponse =response .choices [0 ]#line:564
            log (aiResponse )#line:566
            if (show_response_text ==True ):#line:568
                sendResponseThroughWindow (aiResponse )#line:569
            if (discord_webhook_enabled ==True ):#line:571
                sendResponseThroughWebhook (aiResponse )#line:572
            if (read_response_sound ==True ):#line:574
                readResponse (aiResponse )#line:575
            if (delete_cache_option ==True ):#line:577
                log ("Deleting Cache")#line:578
                os .remove (image_path )#line:579
            log ('Procedure complete. Press ALT+H to show a list of keybinds.')#line:581
        else :#line:582
            logWarning ("'allow_image_sending' is set to False. Set it to True to allow this feature to be used.")#line:583
            time .sleep (.5 )#line:584
    else :#line:586
        if keyboard .is_pressed ('Alt')and keyboard .is_pressed ('`'):#line:587
            image_path =takeScreenshot ()#line:588
            if os .path .exists (image_path ):#line:589
                image =Image .open (image_path ,mode ='r')#line:590
                extractedText =image_to_string (image )#line:591
                log ("SHIT THAT WAS EXTRACTED:")#line:592
                log (extractedText )#line:593
                if (delete_cache_option ==True ):#line:594
                    log ("Deleting Cache")#line:595
                    os .remove (image_path )#line:596
                log ("You are now about the witness the strength of street knowledge. (if the api shit works)")#line:598
                if (override_groq_with_chatgpt !=True ):#line:613
                    log ('Using groq api to get response.')#line:614
                    response =groqClient .chat .completions .create (messages =[{"role":"user","content":extractedText }],model ="llama3-8b-8192",)#line:623
                    aiResponse =response .choices [0 ].message .content #line:625
                else :#line:626
                    log ('Using ChatGPT to get response.')#line:627
                    completion =openAIClient .chat .completions .create (model ="gpt-4o",messages =[{"role":"user","content":"Do not format the response. act like you can read this in a txt."+extractedText }])#line:634
                    aiResponse =completion .choices [0 ].message .content #line:635
                log (aiResponse )#line:636
                if (show_response_text ==True ):#line:637
                    sendResponseThroughWindow (aiResponse )#line:638
                if (discord_webhook_enabled ==True ):#line:640
                    sendResponseThroughWebhook (aiResponse )#line:641
                if (read_response_sound ==True ):#line:643
                    readResponse (aiResponse )#line:644
            else :#line:646
                logError (f"File not found: {image_path}")#line:647
            log ('Procedure complete. Press ALT+H to show a list of keybinds.')
