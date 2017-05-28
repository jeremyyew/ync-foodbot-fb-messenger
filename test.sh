curl -X POST -H "Content-type: application/json" \
-d '{"object":"page","entry":[{"id":"979027202238929","time":1494428871668,"messaging":[{"sender":{"id":"1484887258198358"},"recipient":{"id":"979027202238929"},"timestamp":1494428871158,"message":{"mid":"mid.$cAAN6a6Ui58ZiJCwx9lb8ubp5XBDz","seq":52321,
"text":"testing"}}]}]}' \
http://127.0.0.1:5000/

curl \
--header "Content-type: application/json" \
--request POST \
--data '{"object":"page","entry":[{"id":"979027202238929","time":1494428871668,"messaging":[{"sender":{"id":"1484887258198358"},"recipient":{"id":"979027202238929"},"timestamp":1494428871158,"message":{"mid":"mid.$cAAN6a6Ui58ZiJCwx9lb8ubp5XBDz","seq":52321,
"text":"Dining Hall"}}]}]}' \
http://127.0.0.1:5000/
