class User:
    def __init__(self, username, email,password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Getting email...")
        return self._email

user1=User("alice","Alice@Example.com","password123")

print(user1.email)  # This will trigger the getter and print the email