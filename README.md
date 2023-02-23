# Auto Instagram Memes
 
A python Application that automatically uploads memes from [r/memes](https://www.reddit.com/r/memes/) and sends status notifications to your phone
- - - 

# Working (hopefully) Example: 
[@hourly.memes.4.u](https://www.instagram.com/hourly.memes.4.u/)

# Setup
* ### Download main.py
* ### Run:
```
pip install instagrapi
pip install notify-run
pip install pyinstaller
```
* ### Edit the python file and change the user name password and endpoint variables

* ### In the current directory, run:
```
pyinstaller --onefile main.py
```
* ### After pyinstaller does its job, an exe file will be created in the dist folder.
* ### create a folder called "memes" in the directory, this is where all the memes will be stored. Do not keep the exe file in this folder
- - -

# Keeping the script online 24/7
* ## [Replit](replit.com/)
    * I have tried it but it has not worked for me
* ## Task Scheduler
    * It feels unstable, but here is a tutorial on how to do so: https://techrando.com/2019/06/22/how-to-execute-a-task-hourly-in-task-scheduler/
* ## On your device
    * Edit the given bat file and change **"nameOfFile.exenameOfFile.exe"**
    and **"timeBetweenRunsInSeconds"**
    * Leave this file running on your device (Keep it in another desktop so that it doesn't distrub you)

# Notice: This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Instagram or any of its affiliates or subsidiaries. This is an independent and unofficial Script. There is a chance of your account getting banned or blocked. Use at your own risk. I will not be held responsible for any misuse of this program.