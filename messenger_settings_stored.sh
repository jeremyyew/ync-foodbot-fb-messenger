
EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD


curl -X POST -H "Content-Type: application/json" -d '{
  "persistent_menu":[
    {
      "locale":"default",
      "composer_input_disabled":true,
      "call_to_actions":[
        {
          "title":"Dining Hall",
          "type":"nested",
          "call_to_actions":[
            {
              "title":"DH1",
              "type":"postback",
              "payload":"GET_STARTED_PAYLOAD"
            },
            {
              "title":"DH2",
              "type":"postback",
              "payload":"GET_STARTED_PAYLOAD"
            },
            {
              "title":"DH3",
              "type":"postback",
              "payload":"GET_STARTED_PAYLOAD"
            }
          ]
        },
        {
          "type":"web_url",
          "title":"Other Campus Options",
          "url":"https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
          "webview_height_ratio":"full"
        }
      ]
    }
  ]
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD"

curl -X DELETE -H "Content-Type: application/json" -d '{
  "fields":[
    "persistent_menu"
  ]
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD"