#!/usr/bin/python3

import os
from time import sleep
from datetime import datetime
import picamera
import glob

##############
VID=False #Boolean for pics or video False is pictures, True is videos
NP=2000  #Number of pictures
PWT=10  #Time bewteen pictures in seconds 
VWT=5*60  #Video length in seconds
NV=3    #Number of videos
NPX=1      #Number of picture series
DT=10*60    #Interval between videos in seconds
DTP=0    #Interval between picture series in seconds-0 one series
##############
def picts(wt,M,PTH,N):

	crot= 270
	cres=(1024,768)
	camera=picamera.PiCamera()
	camera.rotation=crot
	camera.resolution=cres
	for i, filename in enumerate(camera.capture_continuous(PTH+'/'+str(M+1)+'-'+'image{timestamp:%H-%M-%S}-{counter:04d}.jpg')):
		sleep(wt)
		if i ==(N-1):
                	break

	camera.close()

###############
def vids(ST,M,PTH):
	camera=picamera.PiCamera()
	ts=PTH+'/'+str(M+1)+"-"+datetime.now().strftime("%H-%M-%S")
	camera.start_recording(ts+'.h264')
	camera.wait_recording(ST)
	camera.stop_recording()
	camera.close()
	print("DONE VIDEO")
##############
def wrtrun():
	with open("NR.TXT","w") as f:
		f.write(str(0))
##############
def main():
	nrl=glob.glob("*.TXT")
	if len(nrl)==0:
		wrtrun()
	

	with open("NR.TXT","r") as f:
		for row in f:
               		nk=int(row)
	NF=nk+1

	with open ("NR.TXT","w") as f:
        	f.write(str(NF))

	PTH="BOOT"+str(NF)
	os.mkdir(PTH)
	
	if VID==False:
		sleep(50)
		for np in range(NPX):
			picts(PWT,np,PTH,NP)
			if DTP>0:
				sleep(DTP)
			else:
				pass
	else:
		sleep(50)
		for nv in range(NV):
			vids(VWT,nv,PTH)
			sleep(DT)
	
	with open("NRLOGS.TXT","w") as f:
		f.write(PTH+" process completed without interruptions")

	os.system("sudo shutdown -h now")  
##############
main()
