import os, re, subprocess
pattern = '(RESOLUTION=1920x1080).+\n(http://.+)'
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in sorted(files):
    media_file = f.replace('.m3u8','.mp4').replace(' ','')
    downloaded = os.path.isfile(media_file)
    if '.mp4' not in f and not downloaded: 
        textfile = open(f, 'r')
        text = textfile.read()
        textfile.close()
        try:
            match = re.search(pattern, text)
            media_url = match.group(2)
            cmdstring = "ffmpeg -i '"+media_url+"' -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 " + media_file
            print(cmdstring)
            print(subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE).stdout.read())
        except:
            print(f)
