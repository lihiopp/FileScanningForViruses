import requests, json, hashlib
global my_apikey

def set_apikey(apikey):
    my_apikey = apikey

    
def scan_file(file_name):
    '''enters the file into Virustotal's queue.'''
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': my_apikey}
    files = {'file': (file_name, open(file_name, 'rb'))}
    response = requests.post(url,files=files, params=params)
    print(response['verbose_msg'])

    
def hash_file(file_name):
    '''hashes the file's data - that's the resource argument needed later.'''
    file = open(file_name, 'rb')
    data = file.read()
    md5_hash = hashlib.md5(data)
    digest = str(md5_hash.hexdigest())
    return digest


def get_report(file_name):
    '''gets the report of the scanned file.'''
    resource = hash_file(file_name)
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': my_apikey, 'resource': resource}
    response = requests.get(url, params=params)
    report = response.json()

    if(report["positives"]>0):
        return "The file is malicious."
    else:
        return "Undetected viruses."
