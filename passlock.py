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

    def save_user(self):
        """
        methode that saves a new user instance into the user list.
        """
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list
    
    def delete_user(self):
        """
        delete account method deletes a saved account from the list
        """
        User.user_list.remove(self)