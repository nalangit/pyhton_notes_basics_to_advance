##-------------------- accessing API__________JUNE_10

# API---------> application programing interface

# server------> used to retrive and send data through code

##                  API----------->REQUEST
##
##
##                  server--------->response code--------------->response data


#  REQUESTS IS THE LIBRARY USED FOR ACCESSING API

##200---> EVERYTHING okay
##
##301--> server redirect to different end point
##
## 400-->  bad request
##
##401---> not authenticated
##
##403---> access forbidden
##
##404----> server not  found
##
##
##503-----> not ready to handle request

##
##import requests
##website=" https://www.google.com/"
##response=requests.get(website)
##print(response)
##
##
##print("---------------------------2")
##
##import requests
##website="http://api.open-notify.org/astros.json"
##response=requests.get(website)
##print(response)
##data = response.json()
##print(data)
##
##import json
##a=json.dumps(data,sort_keys=True,indent=4)
##print(a)


print("----------------------------------------3")

import requests
website="http://api.open-notify.org/iss-pass.json"
parameters={
    "lat":40.71,
    "lon":30
    }
response=requests.get(website,params=parameters)
print(response)
data=response.json()
import json
a=json.dumps(data,sort_keys=True,indent=4)
print(a)
##
##<Response [200]>
##{
##    "message": "success",
##    "request": {
##        "altitude": 100,
##        "datetime": 1654828864,
##        "latitude": 40.71,
##        "longitude": 30.0,
##        "passes": 5
##    },
##    "response": [
##        {
##            "duration": 573,
##            "risetime": 1654844190
##        },
##        {
##            "duration": 653,
##            "risetime": 1654849936
##        },
##        {
##            "duration": 589,
##            "risetime": 1654855805
##        },
##        {
##            "duration": 565,
##            "risetime": 1654861685
##        },
##        {
##            "duration": 631,
##            "risetime": 1654867506
##        }
##    ]
##}

b=data["response"]
print(b)

##[{'duration': 573, 'risetime': 1654844190}, {'duration': 653, 'risetime': 1654849936}, {'duration': 589, 'risetime': 1654855805}, {'duration': 565, 'risetime': 1654861685}, {'duration': 631, 'risetime': 1654867506}]

# ristime alone in o/p:
c=[]
for x in b:
    c.append(x["risetime"])
print(c)

#RISETIME::
##[1654844190, 1654849936, 1654855805, 1654861685, 1654867506]

from datetime import datetime
d=[]
for x in c:
    e=datetime.fromtimestamp(x)
    d.append(e)
print(d)

##[datetime.datetime(2022, 6, 10, 12, 26, 30), datetime.datetime(2022, 6, 10, 14, 2, 16), datetime.datetime(2022, 6, 10, 15, 40, 5), datetime.datetime(2022, 6, 10, 17, 18, 5), datetime.datetime(2022, 6, 10, 18, 55, 6)]

# want output date,month, year format---------


formatt="%d/%m/%y  %H:%M:%S"
for x in d:
    a=datetime.strftime(x,formatt)
    print(a)

    
##10/06/22  12:26:30
##10/06/22  14:02:16
##10/06/22  15:40:05
##10/06/22  17:18:05
##10/06/22  18:55:06
