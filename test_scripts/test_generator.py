import json


def generate_text_test(type, filename, strings, url):
    pre = "curl -X POST -H \"Content-Type: application/json\" -d"
    text_file = open(filename, "w+")

    for string in strings:
        if type == "text":
            payload = {"object": "page", "entry": [{"id": "979027202238929", "time": 1494428871668, "messaging": [
            {"sender": {"id": "1484887258198358"}, "recipient": {"id": "979027202238929"},
             "timestamp": 1494428871158, "message": {"mid": "mid.$cAAN6a6Ui58ZiJCwx9lb8ubp5XBDz", "seq": 52321,
                                                     "text": string}}]}]}
        elif type == "postback":
            payload = {"object": "page", "entry": [{"id": "979027202238929", "time": 1494428871668, "messaging": [
            {"sender": {"id": "1484887258198358"}, "recipient": {"id": "979027202238929"},
             "timestamp": 1494428871158, "postback":{"payload": string}}]}]}
        else:
            print "specify type"
            break
        request = pre + " \'" + json.dumps(payload) + "\' " + url + "\n"
        text_file.write(request)

    text_file.close()
    return

url = "http://127.0.0.1:5000/"
text_list = ["Get Started",
             "info",
             "dh",
             "buttery",
             "amaan",
             "macs",
             "agora",
             "utown",
             "get all",
             "help",
             "feedback",
             "#feedback"]
generate_text_test("text", "test_texts.sh", text_list, url)

generate_text_test("text", "test_help.sh", ["help"], url)
generate_text_test("text", "test_get_started.sh", ["Get Started"], url)

postback_list = ["GET_STARTED_PB",
                 "INFO_PB",
                 "DH_PB",
                 "BUTTERY_PB",
                 "AMAAN_PB",
                 "MACS_PB",
                 "AGORA_PB",
                 "UTOWN_PB",
                 "EXPLORE_PB",
                 "GET_ALL_PB",
                 "FEEDBACK_PB",
                 "COMING_SOON_PB"]
generate_text_test("postback", "test_postbacks.sh", postback_list, url)

# Add permission:  (https://askubuntu.com/questions/38661/how-do-i-run-sh-files)
# chmod +x ./test_texts.sh
# chmod +x ./test_pbs.sh

# ./test_texts.sh
# ./test_pbs.sh
