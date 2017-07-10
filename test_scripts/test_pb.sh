curl \
--header "Content-type: application/json" \
--request POST \
--data '{"object":"page","entry":[{"id":"979027202238929","time":1494428871668,"messaging":[{"sender":{"id":"1484887258198358"},"recipient":{"id":"979027202238929"},"timestamp":1494428871158,"postback":{"payload": "MENU_CHECK_PB"}}]}]}' \
http://127.0.0.1:5000/