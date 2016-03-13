import subprocess
import os
import sys
import re

#69


defaultVal = [
['retries',"--retries", "10"],
['audioFormat','--audio-format',"wav"],
['audioQuality','--audio-quality','192k'],
]

def rip(d):
    # d is our dictionary of required values.
    #In case the dictionary does not define something,
    #we have our own thing to work.
    # defaultVal is our defaultVal dictionary of stuff.
    options = ""
    for i in defaultVal:
        if d.get(i[0],False)==False:
            options = optionAdd(options,i[1],i[2])
        else:
            options = optionAdd(options,i[1],d.get(i[0]))
    #defaultVal stuff to add
    options = optionAdd(options,"--ignore-errors","--extract-audio","-o 'temp.%(ext)s' ","--restrict-filenames")
    command = optionAdd("sudo youtube-dl",options,d['url'])
    #command = "youtube-dl -i " +d['url']+ " --extract-audio --restrict-filenames --audio-format " +"wav"+ " --audio-quality "+"192k"
    print(command)
    subprocess.call(command,shell=True)
    # trimming the file
    subprocess.call("sudo ffmpeg -ss "+d["startTime"]+ " -t "+d["duration"]+" -i temp.wav "+d["filename"]+".wav",shell=True)


    # tiny bit of testing


    #subprocess.call("if [ -f ./temp.wav ]; then rm ./temp.wav")
    #subprocess.call("if [ -f ./input.wav ]; then rm ./input.wav")
    subprocess.call("sudo rm temp.wav",shell=True)
    #subprocess.call("echo 'y \n' ")
    subprocess.call("sudo rm input.wav",shell=True)
    #subprocess.call("echo 'y \n' ")
    #subprocess.call("rm ")





    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, d['filename']+'.wav')
    subprocess.call(['clear'], shell=True)


    return file_out

def optionAdd(*strings):
    s = " "
    returnString = strings[0]

    if len(strings)>1:
        for i in range(1,len(strings)):
            returnString = returnString + s + strings[i]
    return returnString

d = {
'url':'https://www.youtube.com/watch?v=cRpdIrq7Rbo',
'audioFormat':'wav',
'startTime':'0',
'duration':'19',
'filename':'inp'
}
