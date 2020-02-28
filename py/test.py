from login import LoginInformation

instance = LoginInformation()
instance.create_password("xkcd")

print(instance.password)