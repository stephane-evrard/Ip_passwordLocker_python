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

class Credentials():
    """
    Create credential class to help to create new objects of  credentials
    """
    credentials_list = []

    @classmethod
    def verify_user(cls, username, password):
        """
        method to verify whether the user is in our user_list or not.
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user
    
    def __init__(self, account, userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password

    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):
        """
        delete credential method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account):
        """
        method that takes in an account_name and return a credential that matches that account_name.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def copy_password(cls, account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, account):
        """
        method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False