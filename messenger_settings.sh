
curl -X POST -H "Content-Type: application/json" -d '{
  "setting_type":"greeting",
  "greeting":{
    "text":"Hungry? I gotchu fam."
  }
}' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAAZAygcjNS3sBAPG5AC9WEt9FFm3Fi8DZBjb24POoGgm5OpidWyzAJVDHy7bD4ZCsAK9XUzRVnXaCbeopf0RuWaKlvHdvefZBE2SASfivlCPZAC96GBCK9XQCMlVUSkxPxJMxVr7MN3ibJRQ3zJA3ZA7IhjUJ4rT2b7UmAiR5DZAgZDZD"


curl -X POST -H "Content-Type: application/json" -d '{
  "get_started":{
    "payload":"GET_STARTED_PAYLOAD"
  }
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAZAygcjNS3sBAPG5AC9WEt9FFm3Fi8DZBjb24POoGgm5OpidWyzAJVDHy7bD4ZCsAK9XUzRVnXaCbeopf0RuWaKlvHdvefZBE2SASfivlCPZAC96GBCK9XQCMlVUSkxPxJMxVr7MN3ibJRQ3zJA3ZA7IhjUJ4rT2b7UmAiR5DZAgZDZD"