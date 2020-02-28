class PasswordManager:
    """
    Stores an instance of a user-account.
    """

    u_id = 0

    def __init__(self, account_name):
        self.create_id()
        self.account_name = account_name
        self.passwords = []
    
    def add(self, password):
        if password.is_ready:
            self.passwords.append(password)
    
    @classmethod
    def create_id(cls):
        cls.u_id += 1