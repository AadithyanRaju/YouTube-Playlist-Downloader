try:
    import os
    from pytube import YouTube
    import requests
    import re
    import sys
    import termcolor
except:
    import os
    if os.name == 'nt':
        os.system('python -m pip install pytube')
        os.system('python -m pip install termcolor')
        os.system('python -m pip install requests')
        os.system('cls')
    else:
        os.system('python3 -m pip install pytube')
        os.system('python3 -m pip install termcolor')
        os.system('python3 -m pip install requests')
        os.system('clear')
    from pytube import YouTube
    import requests
    import re
    import sys
    import termcolor

def help():
    if os.name == 'nt':
        print('''
usage: python playlistDownloader.py [folderName] [-r 360p/720p] [-h/--help]

folder name: name of the folder where you want to save your videos
             by default it will be the first 5 characters of the 
             playlist title or the playlist id
        
Options:
    -h/--help: to show this help message
    -r: resolution of the video you want to download
        by default it will be 720p
        setable options are 360p and 720p

        ''')
    else:
        print('''
usage: python3 playlistDownloader.py [folder name] [-r 360p/720p] [-h/--help]
folder name: name of the folder where you want to save your videos
             by default it will be the first 5 characters of the 
             playlist title or the playlist id
        
Options:
    -h/--help: to show this help message
    -r: resolution of the video you want to download
        by default it will be 720p
        setable options are 360p and 720p

        ''')
#------------------------------------------------------------------------------
# Main
url=''
user_res=''
if (len(sys.argv)  > 1 ):
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        help()
        sys.exit()
    if '-r' in sys.argv:
        user_res = sys.argv[sys.argv.index('-r') + 1]
        if user_res != '360p' and user_res != '720p':
            print(termcolor.colored('[-]', 'red'),'Incorrect Resolution.')
            sys.exit()

BASE_DIR = os.getcwd()
print('WELCOME TO PLAYLIST DOWNLOADER')
url = str(input("\nPlaylist url: "))
if url == '':
    print(termcolor.colored('[-]', 'red'),'URL cannot be empty!')
    sys.exit()
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
os.chdir(BASE_DIR)
if (len(sys.argv) < 2):
    f_name = f
    f_name = f_name[:5]
else:f_name = sys.argv[1]
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
