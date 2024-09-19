import requests
import base64
import hashlib
import json
import re
import os
from datetime import datetime, timedelta
import time


KEY_URL = "https://poit.bolagsverket.se/poit/rest/HamtaKoppling"
INFO_URL= "https://poit.bolagsverket.se/poit/rest/HamtaKungorelse"

# These are the functions to be used in decoding
def qb(t):
    e = ""
    for n in range(len(t)):
        if '0' <= t[n] <= '9':
            r = ord(t[n]) - ord('0')
            r = (r + 5) % 10
            e += chr(r + ord('0'))
        else:
            e += t[n].lower() if t[n].isupper() else t[n].upper()
    return e

def zb(t, e):
    length = len(t)
    for n in range(length):
        t[n] = (t[n] ^ (e[n & 31] + (e[(n + 8) & 31] ^ e[(n + 17) & 31]))) & 0xFF
        e[n & 31] = (e[n & 31] + (e[(n + 3) & 31] ^ e[(n + 7) & 31])) & 0xFF
        e[n & 31] ^= (e[(n + 12) & 31] + e[(n + 18) & 31]) & 0xFF
    return t
#####This is the function to be used to extract some fields   #####
def extract_value(data, field):
    pattern = f"<b>{field}:</b> (.+?) <br>"
    match = re.search(pattern, data)
    return match.group(1) if match else None
##### This is the function to get the encoding key.
def getHamtaKoppingKey(url):
    response = requests.get(url)
    if(response.status_code==200):
        data = response.text
        print(f'Hamtakoppling:={data}')
        return data
    else:
        print("key generation error")
        return None
counter=0
def getRecordInformation(recId):
    hamtaKey = getHamtaKoppingKey(KEY_URL)
    print(recId,",---,",hamtaKey)
    recId1 = recId.replace("/", "-")
    time.sleep(0.5)
    params={'kungorelseid':recId,'koppling':hamtaKey,'version':'4'}
    headers = {
        'Accept':'application/json, text/plain, */*',
        'accept-encoding':'gzip, deflate, br, zstd',
        'Connection':'keep-alive',
        'Cookie':'_pk_id.1.e7f5=4459834d98728293.1726706485.; _pk_ses.1.e7f5=1; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Afalse%2C%22functional%22%3Afalse%2C%22advertising%22%3Afalse%2C%22timestamp%22%3A1726706511%2C%22type%22%3A%22category%22%2C%22version%22%3A%22286ec2df-e5c4-4a7c-bcf5-9ef6ebc050df%22%7D; TS00000000076=085cfe028fab28009cb80e82da6617a10cae681676832089e24ccadd915a7dbc0fdfa27491ec310b377a275acfe1e2c2088a8bf0d809d000c9df45c800ffc4b7d8cdadc62517f5cb7c73f520b39e893e9b50678b4fc655b7ef0c1646c600eab5e0f942e52fa39a06f1d566a5ceb3278ef61c7a8f582ac516919e27d82a0024fde0c8d197ad1bd3931b7ea650924406c1dbdb1c622fe19aad68a108c1bd99b8ccf6b8c0c0858d4632606cfe8999c9b3e7031a34781f8750f3fad65060cbc543c811e7cb615344b3f877ec6e6d82e38601585fa034483634519864783b936af0e8926ec1f2a1069fc797116900840a16131e8cf7cb1df9a91bd8139e6985b07b204b54a46f139da992; TSPD_101_DID=085cfe028fab28009cb80e82da6617a10cae681676832089e24ccadd915a7dbc0fdfa27491ec310b377a275acfe1e2c2088a8bf0d806380085192a6327da6874633c48f2a37c474b2e48f925c885dd3a711ee08681e320be7eeabcb017cc380fc9c915e66513fde567bd446fc731eab5; TSPD_101=085cfe028fab28008a744c7382cad93ecd8c00dd30174c89c8d1b4a200c0717cb56ba87c3c892161082a3ff0fbc54263081ac81dd90518004f775ad4a587b6f3b01ef615408c8b0ea4bf4de578ff918c; TS6e9892c6077=085cfe028fab280074d4bd68d0ff64f73d703bfe57a811bd5b6e869ab5a3da6289693fde92c740af607ceaf27fde6930089843c9591720009f5d81a21ffce79efac59dc771966eed80325604da2407b3432817ef95042e73; BOL_LB=!fzbiPI6wAk4yLgyNqCTKvztmDanZaw+EbxDOJhNHQV7OOhfnA6roHeKzXCtKQnC6n1CFF25j/Bd8HAI=; TS6e9892c6029=085cfe028fab280025bae4f3207a6666279aa256991ab921d5153a02336012fa61f99b568e1766fc53bbd71ad1093fcc; TS6aeb2efb027=085cfe028fab200005b203a756be11fa7328b26820b9f52c9f4aa945f54b5ae6d42499b92467619808b877ac7f113000173277ea016ff5e3787253fa01b7c6a81a47749760785f577f80f90f2ae01989c591eecde4d2d4971e5b78239af979c0',
        'Host':'poit.bolagsverket.se',
        'Referer':f'https://poit.bolagsverket.se/poit-app/kungorelse/{recId1}',
        'Sec-Ch-Ua-Platform':'Windows',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Security-Request':'required'
    }
    # params={'kungorelseid':"K574499/23",'koppling':"K3943523479111622014",'version':'4'}
    response = requests.get(INFO_URL, headers=headers ,params=params)
    print(response,"=========")
    if(response.status_code==200):
        global counter
        counter+=1
        print("response_data==",response.text,",",counter)
        # encoded_string = response.text
        # r = qb(encoded_string)
        # a = base64.b64decode(r)
        # s = (recId + hamtaKey).encode('utf-8')
        # l = hashlib.sha256(s).digest()
        # e = bytearray(l)
        # a = bytearray(a)
        # o = zb(a, e)
        # # Convert result to a UTF-8 string and then parse JSON
        # o_str = bytes(o).decode('utf-8')
        # d = json.loads(o_str)
        # if d is not None:
        #     kungorelseData = d['kungorelseText']
        # # Extracting values
        # org_nr = extract_value(kungorelseData, "Org nr")
        # if org_nr is None:
        #     org_nr=""
        # foretagsnamn = extract_value(kungorelseData, "Företagsnamn")
        # if foretagsnamn is None:
        #     foretagsnamn=""
        # sate = extract_value(kungorelseData, "Säte")
        # if sate is None:
        #     sate=""
        # post_address = extract_value(kungorelseData, "Postadress")
        # if post_address is None:
        #     e_post=""
        # e_post = extract_value(kungorelseData, "E-post")
        # if e_post is None:
        #     e_post=""
        # typ = extract_value(kungorelseData, "Typ")
        # if typ is None:
        #     typ=""
        # bildat = extract_value(kungorelseData, "Bildat")
        # if bildat is None:
        #     bildat=""
        # if d is not None:
        #     country=d['lan']
        # if d is not None:
        #     published=d['publiceringsDatum']
        # recData = {'publishId':recId,'companyName':foretagsnamn,'registrationNo':org_nr,\
        #         'municipality':sate, 'county':country, 'email':e_post, 'typ':typ,'founded':bildat,'published':published}
        # return recData
    else:
        print("There is not a data to get")
        # return None

# Start and end dates
start_date = datetime(2023, 10, 2)
end_date = datetime(2023, 10, 3)

# URL for the GET request
# url = 'https://poit.bolagsverket.se/poit/rest/SokKungorelse'

# Iterate through each day in the range
current_date = start_date
totalCnt=0
while current_date <= end_date:
    # Format the date as a string in 'YYYY-MM-DD' format
    date_str = current_date.strftime('%Y-%m-%d')
    if os.path.exists(f'{date_str}.json'):
        print(f"{date_str}.json, exists")
        with open(f'{date_str}.json', 'r') as file:
            data = json.load(file)
            # Iterate through the list and print kungorelseid         
            cnt=0
            for entry in data:
                cnt+=1
                totalCnt+=1
                getRecordInformation(entry['kungorelseid'])
                # ExcelRecord = getRecordInformation(entry['kungorelseid'])
                # print(ExcelRecord['publishId'],ExcelRecord['companyName'],ExcelRecord['registrationNo'])                  
                time.sleep(1)
                # print(totalCnt,"=>",cnt,"->",entry['kungorelseid'])
    else:
        print(f"{date_str}.json, does not exist")

    
    # Move to the next day
    current_date += timedelta(days=1)
    
    # Sleep for 1 second to avoid overwhelming the server with requests
    time.sleep(1)

