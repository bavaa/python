#by mama
import sys
from os import path
from subprocess import call
from time import sleep
def setup():
    call("cd ~",shell=True)
    if (not path.exists("gdrive-linux-x64")):
        call("sudo apt install -y aria2",shell=True)
        call("aria2c https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download",shell=True)
        sleep(5)
    else :
        call("aria2c https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download",shell=True)
        sleep(5)
    if (path.exists("gdrive-linux-x64")):
        print("gdrice-linux-x64 already exists :  ")
        call("mv gdrive-linux-x64 gdrive",shell=True)
        call("chmod +x gdrive",shell=True)
        call("sudo install gdrive /usr/local/bin/gdrive",shell=True)
        call("clear",shell=True)
        call("gdrive list",shell=True)
    else :
        print("delete existing gdrive file")
def screen():
    call("clear",shell=True)
    print("Tap space to continue in the next screen :  ")
    call("sudo apt install -y screen",shell=True)
    call("screen")
    call("screen -x")
    menu()
def menu():
    call("clear",shell=True)
    print("Gdrive uploader script by 'rowdy mama'  ")
    print("Opton we currently have  ")
    print("1. installation  ")
    print("2. Download the file you want  ")
    print("3. Upload the file to Gdrive  ")
    print("4. Exit  ")
    selection = input("Select your choice :  ")
    if(selection==1):
        setup()
    if(selection==2):
        download()
    if(selection==3):
        upload()
    if(selection==4):
        sys.exit()
def download():
    call("clear",shell=True)
    print("What do you want to download ")
    print("1. From url  ")
    print("2. From torrent  ")
    dwn_type = input()
    if (dwn_type == 1):
        call("sudo apt install -y aria2",shell=True)
        call("clear",shell=True)
        input_url=input("Enter your URL")
        url = "aria2c -x10 "
        url=url+input_url
        call(url,shell=True)
    if (dwn_type=2):
        call("sudo apt install -y transmission-cli",shell=True)
        magnet_link=input("Enter the magnet linf of the torrent file :  ")
        torrent="transmission-cli -b "
        torrent=torrent + magnet_link
        call(torrent,shell=True)

def upload():
    call("clear",shell=True)
    upload_file_name=input("Enter the file name you want to upload :  ")
    upload_file="gdrive upload "
    upload_file=upload_file+upload_file_name
    call(upload_file,shell=True)


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
#by barack obama (arc_total)    
'''import os
from time import sleep
import subprocess
from subprocess import STDOUT
def gdrive():
    os.popen("cd ~")
    if (not os.path.exists("gdrive-linux-x64")):
        subprocess.call('sudo apt-get install -y aria2', shell=True)
        #proc.wait()
        #os.popen("sudo apt install -y aria2")
        subprocess.call("aria2c https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download --on-bt-download-complete=exit",shell=True)
    else :
        os.popen("aria2c https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download")
    sleep(5)
    subprocess.call("mv gdrive-linux-x64 gdrive",shell=True)
    subprocess.call("sudo chmod +x gdrive",shell=True)
    subprocess.call("sudo install gdrive /usr/local/bin/gdrive",shell=True)
    subprocess.call("gdrive list",shell=True)
    '''file = open("abc.txt","w")
    file.write(activation_link)
    file.close()'''

gdrive()
'''
