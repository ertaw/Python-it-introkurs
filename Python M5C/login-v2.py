

def login(users):
    while 1==1:
       user = input("\nUser:")
       password = input("Password:")
       if user in users:
           if password in users[user]:
               # print("\nWelcome", user)
               return user
       else:
           print("\nInvalid username or password")
          
    
    
    
users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user1 = login(users1)
print(f"Welcome {user1}")

users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print(f"Welcome {user2}")