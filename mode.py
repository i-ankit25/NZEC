import os
import subprocess as sp
import time
extProc2 = sp.Popen(['python','pi-object-detection_new/pi_object_detection.py'])
while(True):
		open('/home/ankit/NZEC/search.txt','r')
                f1 = f.readline().rstrip('\n')
                if f1=="model":
			sp.Popen.terminate(extProc1)
			extProc2 = sp.Popen(['python','broadcast.py']) 

		elif f1=="human":
			sp.Popen.terminate(extProc2)
			extProc2 = sp.Popen(['python','pi-object-detection_new/pi_object_detection.py'])
		time.sleep(5)
