import requests
import os
import time
from colorama import init
from colorama import Fore, Back, Style
my_api_id = '158d290e'
my_api_key=  '6192c53aa8807df16ad4f00b76bf7b00'
tfl_api_id = 'YOUR_API_ID'
tfl_api_key = 'YOUR_API_KEY'
#print(tfl1)
my_url = 'https://api.tfl.gov.uk/Line/Mode/tube/Status?detail=false&app_id='+my_api_id+'&app_key='+my_api_key
while True:
    tfl1 = requests.get(my_url).json()
    print(tfl1[0]['name']+ ' --> ' + tfl1[0]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[1]['name']+ ' --> ' + tfl1[1]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[2]['name']+ ' --> ' + tfl1[2]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[3]['name']+ ' --> ' + tfl1[3]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[4]['name']+ ' --> ' + tfl1[4]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[5]['name']+ ' --> ' + tfl1[5]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[6]['name']+ ' --> ' + tfl1[6]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[7]['name']+ ' --> ' + tfl1[7]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[8]['name']+ ' --> ' + tfl1[8]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[9]['name']+ ' --> ' + tfl1[9]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[10]['name']+ ' -->' + tfl1[10]['lineStatuses'][0]['statusSeverityDescription'])
    print('Bakerloo Line --> ' +tfl1[0]['lineStatuses'][0]['statusSeverityDescription'])
    time.sleep(10)
    os.system('cls')

# [API ATTEMPT BY MICHAEL PERES]
