import os
import subprocess as sp
import time

extProc1 = sp.Popen(['python','pi_object_detection.py']) 

os.environ['PREV']='1'
os.environ['CURRENT']='1'

while(True):
		if(os.environ['PREV']=='1' and os.environ['CURRENT']=='0'):
			sp.Popen.terminate(extProc1)
			extProc2 = sp.Popen(['python','broadcast.py']) 
			os.environ['PREV']=0

		elif (os.environ['PREV']=='0' and os.environ['CURRENT']=='1'):
			sp.Popen.terminate(extProc2)
			extProc2 = sp.Popen(['python','pi_object_detection.py'])
			os.environ['PREV']=1
