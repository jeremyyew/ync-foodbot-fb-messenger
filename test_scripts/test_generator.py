import json

def generate_text_test(type, filename, payloads, url):
    pre = "curl -X POST -H \"Content-Type: application/json\" -d"
    text_file = open(filename, "w+")
    if type == "text":
        for payload in payloads:
            request = pre + " \'" + json.dumps(payload) + "\' " + url + "\n"
            text_file.write(request)
        text_file.close()
        return

    elif type == "postback":
        return

    else:
        print "please specify type"
        return


url = "http://127.0.0.1:5000/"
feedback_text = {"object":"page","entry":[{"id":"979027202238929","time":1494428871668,"messaging":[{"sender":{"id":"1484887258198358"},"recipient":{"id":"979027202238929"},"timestamp":1494428871158,"message":{"mid":"mid.$cAAN6a6Ui58ZiJCwx9lb8ubp5XBDz","seq":52321,
"text":"#feedback"}}]}]}
generate_text_test("text", "test_texts.sh", [feedback_text], url)

# Add permission:  (https://askubuntu.com/questions/38661/how-do-i-run-sh-files)
# chmod +x ./test_texts.sh
# chmod +x ./test_pbs.sh

# ./test_texts.sh
# ./test_pbs.sh
