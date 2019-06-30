'''import os
def gdrive():
    os.popen("cd ~")
    if (not os.path.exists("gdrive-linux-x64")):
        os.popen("sudo apt install -y aria2")
        os.popen("aria2c https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download")
    else :
        os.popen("aria2c https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download")
    os.popen("mv gdrive-linux-x64 gdrive")
    os.popen("chmod +x gdrive")
    os.popen("sudo install gdrive /usr/local/bin/gdrive")
    os.popen("gdrive list")
    '''file = open("abc.txt","w")
    file.write(activation_link)
    file.close()'''

gdrive()
'''

    
//by barack obama (arc_total)    
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
