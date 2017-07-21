#!/usr/bin/env bash

curl -X POST -H "Content-Type: application/json" -d '{
  "setting_type":"greeting",
  "greeting":{
    "text":"Hungry? I gotchu fam."
  }
}' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD"


curl -X POST -H "Content-Type: application/json" -d '{
  "setting_type":"call_to_actions",
  "thread_state":"new_thread",
  "call_to_actions":[
    {
      "payload":"GET_STARTED_PB"
    }
  ]
}' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD"


curl -X POST -H "Content-Type: application/json" -d '{
  "setting_type":"call_to_actions",
  "thread_state":"existing_thread",
  "call_to_actions": [
        {
          "type": "postback",
          "title": "What\u0027s cooking?",
          "payload": "MENU_CHECK_PB"
        },
        {
          "type": "postback",
          "title": "Order from buttery",
          "payload": "CENDANA_BUTTERY_ORDER_PB"
        },
        {
          "type": "postback",
          "title": "Discover new food",
          "payload": "COMING_SOON_PB"
        }
      ],
}' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD"
