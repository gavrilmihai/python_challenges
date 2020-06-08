import os
import time
from webexteamssdk import WebexTeamsAPI
os.environ["WEBEX_TEAMS_ACCESS_TOKEN"] = "OGM1OGVjNmQtNTkwNC00YmE1LWJhZGUtOTI2MmMzNDIxZGM5MWE3Y2FhMTEtNGY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
ACCESS_TOKEN = 'OGM1OGVjNmQtNTkwNC00YmE1LWJhZGUtOTI2MmMzNDIxZGM5MWE3Y2FhMTEtNGY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f' 
api = WebexTeamsAPI(ACCESS_TOKEN)

#==============================================================================

message = "Hi SDA Community Member, </br></br>this is just a reminder of the SDA EMEAR Bi-Weekly Community Call taking place tomorrow at 14:00 CEST.</br></br>https://cisco.webex.com/cisco/j.php?MTID=mbb9eeff56ed0b457096ea90aa61fff7</br></br>Our agenda for this week is:</br>-Community Updates (TAC/TTG/CXPM/BU/CSS Teams)</br>-Project Overview / Challenges GSK (Dhrumil)</br>-Update and overview of ongoing UKI Projects</br>-Field challenges encountered with 9800 WLC</br>-Using IOL to Simulate SDA Topologies</br>-AOB</br></br>Should you have any last minute topics that need discussion, please make sure to use our smartsheet form to add your item: http://go2.cisco.com/sdacxbiweekly</br></br>Looking forward to seeing you there."
banner = "cx_sda_banner.jpg"

#==============================================================================

filepath = 'cx_sda_member_list_FULL.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       email = line.strip()+"@cisco.com"
       print("Target receiver " + format(cnt) + " --> " + email)
       line = fp.readline()
       cnt += 1
       time.sleep(0.01)
fp.close()
print (" ")
print (" ")
print ("===========================================================================================")
print ("Webex Team mesage will be sent to the list above in 10 sec unless you stop the script now!!")
print ("===========================================================================================")
print (" ")
print (" ")

time.sleep(10)

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
        email = line.strip()+"@cisco.com"
        try:
            api.messages.create(toPersonEmail=email, markdown=message, files=[banner])
        except:
            pass  
        print ('Sent message to ' + email)       
        line = fp.readline()
        cnt += 1
        time.sleep(2)
       