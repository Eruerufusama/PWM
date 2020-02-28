from passlib.hash import sha256_crypt as sha2
from password import generate_password

class LoginInformation:
    """
    Stores an instance of login-information, including encrypted password.
    """
    i = 0
    def __init__(self):
        self.u_id = self.i
        self.iterate_id()
        self.password = None # IMPORTANT - stores only encrypted version of password.
        self.username = None
        self.email = None
        self.assignment = None # Website/application/etc.

    def create_password(self, method=None):
        NOT_ENCRYPTED = generate_password(method)
        return sha2.encrypt(NOT_ENCRYPTED)
        

    @classmethod
    def iterate_id(cls):
        cls.i += 1