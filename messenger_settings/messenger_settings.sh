curl -X POST -H "Content-Type: application/json" -d '{"greeting": {"text": "Hungry? I gotchu fam."}, "setting_type": "greeting"}' https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD
curl -X POST -H "Content-Type: application/json" -d '{"call_to_actions": [{"payload": "GET_STARTED_PB"}], "thread_state": "new_thread", "setting_type": "call_to_actions"}' https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD
curl -X POST -H "Content-Type: application/json" -d '{"call_to_actions": [{"type": "postback", "payload": "MENU_CHECK_PB", "title": "What\\u0027s cooking?"}, {"type": "postback", "payload": "CENDANA_BUTTERY_ORDER_PB", "title": "Order from buttery"}, {"type": "postback", "payload": "COMING_SOON_PB", "title": "Discover new food"}], "thread_state": "existing_thread", "setting_type": "call_to_actions"}' https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD
