from subprocess import Popen,PIPE
def torrent_link (link):
    process=Popen(["aria2c", "--seed-time=0", link],stdout=PIPE,stderr=PIPE)
    if process.stderr.read() is not None:
        print(process.stdout.read())
    else:
        print(process.stdout.read())

def url_link (link):
    #process=Popen(["aria2c", "-x4", "-k1M", link],stdout=PIPE,stderr=PIPE)
    process=Popen(["wget",link],stdout=PIPE,stderr=PIPE)
    process_out=process.stdout.read()
    proecss_err=process.stderr.read()
    if process.stderr.read() is not None:
        print("error")
        print(proecss_err)
    else:
        print("output")
        print(process_out)

link=str(input("enter the link"))
print(link)
if link.startswith("magnet:?"):
    torrent_link(link)
    
else:
    url_link(link)
