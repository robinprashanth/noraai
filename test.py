
import os
import datetime
ts = datetime.datetime.now()
import glob
import re
import time, os, fnmatch, shutil

t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
BACKUP_NAME = ("backup-" + timestamp)

print(os.path.join(os.getcwd(), 'recordings'))

filename = ts.strftime("%Y-%m-%d%H%M%S")
f = open(f"{filename}.wav", "x")
f.close()

print('Named explicitly:')
dire = os.path.join(os.getcwd(), 'recordings', '*')
tt = glob.iglob(dire)
files = sorted(tt, key=os.path.getctime, reverse=True)
ff = 'D:\\myprojects\\openai-whisper-voice-commands\\recordings\\2023-01-20130813.wav'
gg = re.sub("\/\/", "\/", ff)
print(gg)
print(files)
for name in glob.glob(dire):
    print(name)