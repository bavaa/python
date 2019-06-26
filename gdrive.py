import os
def gdrive():
    os.popen("cd ~")
    os.popen("rm -rf uc\?id\=0B3X9GlR6EmbnWksyTEtCM0VfaFE")
    if (not os.path.exists("uc\?id\=0B3X9GlR6EmbnWksyTEtCM0VfaFE")):
        os.popen("sudo apt install wget")
        os.popen("wget https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download")
    os.popen("mv uc\?id\=0B3X9GlR6EmbnWksyTEtCM0VfaFE gdrive")
    os.popen("chmod +x gdrive")
    os.popen("sudo install gdrive /usr/local/bin/gdrive")
        activation_link = os.popen("gdrive list")
    file = open("abc.txt","w")
    file.write(activation_link)
    file.close()

gdrive()
