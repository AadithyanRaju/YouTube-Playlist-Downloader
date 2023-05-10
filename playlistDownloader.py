ts=input("Troubleshoot? (y/n): ")
if ts.lower()[0] == 'y':
    import os
    if os.name == 'nt':
        os.system('python -m pip install -U pip')
        os.system('python -m pip install -U pytube')
        os.system('python -m pip install -U termcolor')
        os.system('python -m pip install -U requests')
        os.system('cls')
    else:
        os.system('python3 -m pip install -U pip')
        os.system('python3 -m pip install -U pytube')
        os.system('python3 -m pip install -U termcolor')
        os.system('python3 -m pip install -U requests')
        os.system('clear')
from pytube import YouTube
import requests
import re
import sys
import termcolor
def folderName(name:str):
    r = ''
    for i in name:
        if i.isalnum():
            r += i
        elif i == ' ':
            r += '_'
    return r
url=''
user_res=''
BASE_DIR = os.getcwd()
print('WELCOME TO PLAYLIST DOWNLOADER')
url = str(input("\nPlaylist url: "))
if url == '':
    print(termcolor.colored('[-]', 'red'),'URL cannot be empty!')
    sys.exit()
user_res = str(input("Resolution (720p/360p)(default:720p): "))
if user_res == '':user_res = "720p"
our_links = []
try:req = requests.get(url)
except:
    print(termcolor.colored(('[-]'), 'red'), 'no internet')
    exit()
text = req.text
if 'list=' in url:
    eq = url.rfind('=') + 1
    f = url[eq:]
else:
    print(termcolor.colored('[-]', 'red'),'Incorrect Playlist.')
    exit()
temp = re.compile(r'watch\?v=\S+?list=' + f)
mat = re.findall(temp, text)
for m in mat:
    a = m.replace('&amp;', '&')
    b = 'https://youtube.com/' + a
    if b not in our_links:our_links.append(b)
if our_links == False:sys.exit()
print(termcolor.colored('[+]', 'green'), 'Playlist Link Detected')
f_name = str(input("Folder name: "))
if f_name == '':
    print(termcolor.colored('[-]', 'red'),'Folder name cannot be empty!')
    sys.exit()
f_name = folderName(f_name)
os.chdir(BASE_DIR)
try:os.mkdir(f_name)
except:print(termcolor.colored('[-]', 'yellow'), 'Folder already exists')
os.chdir(f_name)
SAVEPATH = os.getcwd()
print(termcolor.colored('[+]', 'green'),end='')
print(f' Saving to : {SAVEPATH}')
x=[]
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        pathh = os.path.join(root, name)        
        if os.path.getsize(pathh) < 1:os.remove(pathh)
        else:x.append(str(name))
print(termcolor.colored('[*]', 'yellow'),'connecting . . .')
for link in our_links:
    while True:
        try:
            yt = YouTube(link)
            file = yt.title
            file = file + '.mp4'
            file = file.replace('|', '')
            break
        except:print(termcolor.colored('[-]', 'red'), 'Connection problem.. Retrying')
    if file not in x:
        vid = yt.streams.filter(progressive=True, file_extension='mp4', res=user_res).first()
        print(termcolor.colored('[+]', 'blue'),'Downloading : ' + vid.default_filename)
        print(termcolor.colored('[+]', 'blue'),'size : ' + str(round(vid.filesize / (1024 * 1024), 2)) + ' MB.')
        vid.download(SAVEPATH)
        print(termcolor.colored('[+]', 'green'),'Downloaded')
    else:print(termcolor.colored('[+]', 'yellow'),'Already downloaded : ' + file)
print(termcolor.colored('[*]','green'),'Downloading Finished')
print(termcolor.colored('[*]','green'),'Save to : ' + SAVEPATH)
