import os
def gdrive():
    os.popen("cd ~")
    os.popen("aria2c https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download")
    if (not os.path.exists("gdrive-linux-x64")):
        os.popen("sudo apt install -y aria2")
        os.popen("aria2c https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download")
    os.popen("mv gdrive-linux-x64 gdrive")
    os.popen("chmod +x gdrive")
    os.popen("sudo install gdrive /usr/local/bin/gdrive")
    os.popen("gdrive list")
    '''file = open("abc.txt","w")
    file.write(activation_link)
    file.close()'''

gdrive()
