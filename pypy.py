from pathlib import Path
import shutil
import os
import subprocess

out_dir="out"
dirpath = Path(out_dir)
if dirpath.exists() and dirpath.is_dir():
	shutil.rmtree(dirpath)
os.mkdir(dirpath)

last=1
for i in range(last,1000):
	if os.path.isdir(str(i)):
		last=i
	else:
		break
print(last)



def reky(cate,lista):
	if(len(lista)==cate):
		concky='_'.join(lista)
		concky=concky.replace(".png", "_")
		concky=concky.replace("/", "_")
		strToCal=["magick.exe","convert"]+lista+["-flatten","out/"+concky+".png"]
		subprocess.call(strToCal)
		return
	folder=str(len(lista)+1)
	for file in os.listdir(folder):
		reky(cate,lista+[folder+"/"+file])

reky(last,[])