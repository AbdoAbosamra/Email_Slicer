email = input("Please Enter your Email : ")
components = email.split("@")
username = components[0]
domain = components[1]
print(f"The username for this user is  : {username}")
print(f"The domain for this email is : {domain}")
