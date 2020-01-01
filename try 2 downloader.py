from subprocess import Popen,PIPE,STDOUT
def torrent_link (link):
    process=Popen(["aria2c", "--seed-time=0", link],stdout=PIPE,stderr=PIPE)
    if process.stderr.read() is not None:
        print(process.stdout.read())
    else:
        print(process.stdout.read())
def url_link (link):
    from subprocess import Popen,PIPE,STDOUT
    #process=Popen(["aria2c", "-x4", "-k1M", link],stdout=PIPE,stderr=PIPE)
    process=Popen(["wget",link],stdout=PIPE,stderr=STDOUT)
    while True:
        output = process.stdout.readline()
        if output == b"" and process.poll() is not None:
            return
        if output:
            print(output.decode("utf-8").strip())
link=str(input("enter the link"))
if link.startswith("magnet:?"):
    torrent_link(link)
    
else:
    url_link(link)
