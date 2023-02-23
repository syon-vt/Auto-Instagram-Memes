# imports
from requests import get
from urllib.request import urlretrieve
from instagrapi import Client
from notify_run import Notify
from datetime import datetime

# configures notify-run to send notifications to your phone
#Click create a channel on: https://notify.run/
endpoint = ""
noti = Notify(endpoint=endpoint)

# credentials
user = 'hourly.memes.4.u'
passwd = ''

# initialize and login to Instagram
cl = Client()
try:
    cl.login(user, passwd)
    noti.send("Login Successful")
except:
    noti.send("Login Failed Check the Instagram App")

def save_image():

    # get meme information as json
    api = 'https://api.pymeme.repl.co'
    meme = get(api).json()

    # save meme informtion as dictionary and save image to memes folder
    meme_dict = meme.get("meme")
    img_url = meme_dict.get("image url")
    urlretrieve(img_url, "memes/"+meme_dict.get("title")+".jpg")
    print("Image Saved")

    # upload image to Instagram with caption
    image = "memes/"+meme_dict.get("title")+".jpg"
    captiont = " "+meme_dict.get("title")+"\n \n Credit(Reddit): "+meme_dict.get(
        "author")+"\n \n \n #meme #funny #dankmemes #reddit #memepage #memesdaily #memeshourly"
    cl.photo_upload(image, captiont)

# runs the function twice incase it fails the first time
# exits the program if it fails twice
try:
    save_image()
    noti.send("Image Uploaded")
    print("Image uploaded on first try at " +
          datetime.now().strftime("%H:%M:%S"))
except:
    noti.send("Upload Failed once Retrying...")
    print("Image Upload failed Retrying...")
    try:
        save_image()
        noti.send("Image Uploaded")
        print("Image uploaded on second try")

    except:
        noti.send("Image upload failed twice Check the Instagram App")
        print("Image upload failed twice Check the Instagram App")
        print(datetime.now().strftime("%H:%M:%S"))
        
#logs out of Instagram
cl.logout()
