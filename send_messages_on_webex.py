import os
import time
from webexteamssdk import WebexTeamsAPI
os.environ["WEBEX_TEAMS_ACCESS_TOKEN"] = "OGM1OGVjNmQtNTkwNC00YmE1LWJhZGUtOTI2MmMzNDIxZGM5MWE3Y2FhMTEtNGY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
ACCESS_TOKEN = 'OGM1OGVjNmQtNTkwNC00YmE1LWJhZGUtOTI2MmMzNDIxZGM5MWE3Y2FhMTEtNGY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f' 
api = WebexTeamsAPI(ACCESS_TOKEN)

#==============================================================================

message = "**Test5**"
banner = "grusu.jpg"

#==============================================================================

print (" ")
print (" ")
print ("===========================================================================================")
print ("Webex Team mesage will be sent to the list above in 10 sec unless you stop the script now!!")
print ("===========================================================================================")
print (" ")
print (" ")
time.sleep(2)

email="grusu@cisco.com"
roomid="Y2lzY29zcGFyazovL3VzL1JPT00vMmFlZWYxODAtOTEzOC0xMWVhLWJkNzYtNzkwNjdmYzRhOGRl"
try:
    api.messages.create(toPersonEmail=email, markdown=message)
    api.messages.create(roomid,markdown=message ,files=[banner])
except:
    pass  
print ('Sent message to ' + email)       
print ('Sent message to ' + roomid)       
