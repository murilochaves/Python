from firebase import firebase

firebase = firebase.FirebaseApplication('https://pythoncomfirebase.firebaseio.com/', None)

result = firebase.get('/usuario', None)

print (result)