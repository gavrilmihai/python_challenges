#python script to send messages on webex teams using boot https://developer.webex.com/my-apps/dnac-bru
import requests
import os
import time


#==============================================================================
bot_token = 'OGM1OGVjNmQtNTkwNC00YmE1LWJhZGUtOTI2MmMzNDIxZGM5MWE3Y2FhMTEtNGY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
text = "test message"
email = "grusu@cisco.com"
#==============================================================================


url = "https://webexapis.com/v1/messages"

payload = "{\r\n \"toPersonEmail\" : email(),\r\n \"text\" : \"hi from Postman\"\r\n}"
headers = {
'Authorization': 'Bearer OGM1OGVjNmQtNTkwNC00YmE1LWJhZGUtOTI2MmMzNDIxZGM5MWE3Y2FhMTEtNGY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f',
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))