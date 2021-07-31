import random
import string
import pyperclip

class User:
    """
    Create new user that generates new instances of a user.
    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines the property of a user.
        """
        self.username = username
        self.password = password