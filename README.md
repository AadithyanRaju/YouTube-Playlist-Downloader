# YouTube-Playlist-Downloader<hr>
Download your any YouTube playlist with a single URL.
<hr>
### Requirements

* python 3.5 or above
* packages

  * termcolor
  * pytube
  * requests
<hr>
### Usage

* Windows

  ```
  $ python playlistDownloader.py [folderName] [-r 360p|720p] [-h/--help]
  ```
* Linux

  ```
  $ python3 playlistDownloader.py [folderName] [-r 360p|720p] [-h/--help]
  ```


folderName: name of the folder where you want to save your video by default it will be the first 5 characters of the playlist title or the playlist id

Options:

    -h/--help: to show this help message

    -r: resolution of the video you want to download by default it will be 720p setable options are 360p and 720p

---
