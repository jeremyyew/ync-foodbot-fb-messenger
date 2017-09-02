from firebase import firebase
firebase = firebase.FirebaseApplication('https://ync-foodbot-server.firebaseio.com/', None)
result = firebase.get('/content', "dh_text")
print result

new_content = "hello lol"
result = firebase.post('/content', new_content)
print result