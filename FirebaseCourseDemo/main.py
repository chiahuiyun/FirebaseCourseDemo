import pyrebase
import urllib

firebaseConfig = {
    'apiKey': "AIzaSyClWQb5Ah2DBekOU9nPvJ_x0Iprg0F0290",
    'authDomain': "fir-course-a4f20.firebaseapp.com",
    'projectId': "fir-course-a4f20",
    'storageBucket': "fir-course-a4f20.appspot.com",
    'messagingSenderId': "359142383403",
    'appId': "1:359142383403:web:8ab4ed56e61adde622ef6e",
    'measurementId': "G-RWW09YSDB6",
    'databaseURL': "https://fir-course-a4f20-default-rtdb.asia-southeast1.firebasedatabase.app/"
    }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
#auth = firebase.auth()
#storage = firebase.storage()

#Authentication
#Login
#email = input("Enter your email: ")
#password = input("Enter your password: ")
#try:
#    auth.sign_in_with_email_and_password(email, password)
#    print("Successfully signed in!")
#except:
#    print("Invalid user or password. Try again.")

#Sign Up
#email = input("Enter your email: ")
#password = input("Enter your password: ")
#confirmpass = input("Confirm passwird: ")
#if password == confirmpass:
#    try:
#        auth.create_user_with_email_and_password(email, password)
#        print("Success!")
#    except:
#        print("Email already exits")


#Storage
#upload
#filename = input("Enter the name of the file you want to upload: ")
#cloudfilename = input("Enter the name of the file on the cloud: ")
#storage.child(cloudfilename).put(filename)

#print(storage.child(cloudfilename).get_url(None))

#download
#cloudfilename = input("Enter the name of the file you want to download: ")
#storage.child("google.txt").download("", "download.txt")

#reading file
#cloudfilename = input("Enter the name of the file you want to download: ")
#url = storage.child(cloudfilename).get_url(None)
#f = urllib.request.urlopen(url).read()
#print(f)

#Database
#data = {'age': 32, 'address': "LA", 'employed': False, 'name': "Jane"}
#db.child("people").push(data)
# set own id
#db.child("people").child("dahjsak").set(data)

#Update
#db.child("people").child("dahjsak").update({'name': 'Jane'})

#people = db.child("people").get()
#for person in people.each():
#    if person.val()['name'] == 'Mark':
#        db.child("people").child(person.key()).update({'name': 'Jane'})

#Delete
#db.child("people").child("person").remove()

#people = db.child("people").get()
#for person in people.each():
#    if person.val()['name'] == 'John Smith':
#        db.child("people").child(person.key()).child("age").remove()

#Read
#people = db.child("people").order_by_child("age").equal_to(32).get()
#people = db.child("people").order_by_child("name").equal_to("Jane").get()
#people = db.child("people").order_by_child("age").start_at(25).get()
#people = db.child("people").order_by_child("age").start_at(25).end_at(30).get()
#people = db.child("people").order_by_child("employed").equal_to(True).get()
#people = db.child("people").order_by_child("employed").equal_to(True).limit_to_first(1).get()
people = db.child("people").order_by_child("employed").equal_to(False).limit_to_last(1).get()

for person in people.each():
    #print(person.val()['address']) # t get only address
    print(person.val())



