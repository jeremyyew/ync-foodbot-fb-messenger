import sys
import requests, json

test_text = sys.argv[1]

url = "http://127.0.0.1:5000/"
headers = {'content-type': 'application/json'}

if test_text == "test_all":
    text_list = ["Get Started",
                 "dh",
                 "buttery",
                 "amaan",
                 "macs",
                 "agora",
                 "utown",
                 "get all",
                 "share",
                 "help",
                 "feedback",
                 "#feedback"]
    for text in text_list:
        payload = {"object": "page", "entry": [{"id": "979027202238929", "time": 1494428871668, "messaging": [
            {"sender": {"id": "1484887258198358"}, "recipient": {"id": "979027202238929"},
             "timestamp": 1494428871158, "message": {"mid": "mid.$cAAN6a6Ui58ZiJCwx9lb8ubp5XBDz", "seq": 52321,
                                                     "text": text}}]}]}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print r.text
        if r.status_code != requests.codes.ok:
            print r.text

else:
    payload = {"object": "page", "entry": [{"id": "979027202238929", "time": 1494428871668, "messaging": [
                {"sender": {"id": "1484887258198358"}, "recipient": {"id": "979027202238929"},
                 "timestamp": 1494428871158, "message": {"mid": "mid.$cAAN6a6Ui58ZiJCwx9lb8ubp5XBDz", "seq": 52321,
                                                         "text": test_text}}]}]}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print r.text
    if r.status_code != requests.codes.ok:
        print r.text


