from requests import request
import hashlib, time, os, sys

API_KEY = "e5f3fab2a68932aff378a248f0288ba3de03d748a92f6d2453906e35d4dfb905"
ScanUrlVar = "https://www.virustotal.com/vtapi/v2/file/scan"
ReportUrlVar = "https://www.virustotal.com/vtapi/v2/file/report"
ServerUrlVar = "http://127.0.0.1:8080/api/add"
BASE_FILES = dict()
MAX_PERCENTAGE = 0

#Scan for new BASE_FILES
while True:
	time.sleep(5)
	#Iterate through every file in the current directory
	for fname in os.listdir("."):
		try:
			if os.path.isfile(fname):
				fstate=open(fname,"rb")
				fcontent=fstate.read()
				fstate.close()
				md5 = hashlib.md5(fcontent).hexdigest()
				if md5 not in BASE_FILES.values():
					#Uploading File
					params = {"apikey":API_KEY}
					files = {"file":(fname,fcontent)}
					response = request("POST", ScanUrlVar, files=files, params=params).json()
					resource = response["resource"]
					time.sleep(30)
					#Retrieving File Report
					params = {"apikey":API_KEY,"resource":resource}
					response = request("GET", ReportUrlVar, params=params).json()
					#Calculate percentage
					total = response["total"]
					positives = response["positives"]
					percentage = positives / total * 100   
					#Save/Delete file 
					if percentage >= MAX_PERCENTAGE:
						print("Delete File")
						#os.remove(fname)
						data = {"data":"Not Allowed: <filename> with MD5 Checksum: <md5>"}
						request("POST", ServerUrlVar, data=data)
					else:
						print("Save File")
						BASE_FILES.update({fname:md5})
						data = {"data":"Allowed: <filename> with MD5 Checksum: <md5>"}
						request("POST", ServerUrlVar, data=data)
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno)
			pass
