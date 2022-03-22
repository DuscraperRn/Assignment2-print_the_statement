import os
import sys
import subprocess

dir_path=os.path.dirname(os.path.realpath(__file__))

try:
	F=open(dir_path+'/Assignment2/start_assignment.log').read().split('\n')
	F.pop()
except Exception as E:
	sys.exit('Exception occured during configuration read.\n Exiting application...')
C1=0
C2=0

for i in F:
	if 'beginning of assignment' in i:
		C1=1
	if C1==1: #C1=1 i.e "beginning of assignment" pattern has already occured
		if 'required_pattern_' in i:
			C2=1
	if C2==1: #C2=1 i.e pattern "required_pattern_" has been occured
		try:
			f_name=i.split(' ')[-1].strip()	# taking file name from occured line 
		except Exception as e:
			print('Exception Occured during file name fetching'+str(e))
		try:
			subprocess.check_output('grep "assignment_completed" -A1 '+dir_path+'/Assignment2/Logs/'+f_name+'|tail -1',shell=True)
			sys.exit('Print Execution completed !!!')
		except Exception as e:
			sys.exit('Exception Occured '+str(e))