from passlock import User, Credentials

def function():
	print("               ____                         _____  _                               ")
	print("              |  _ \                       / ____|| |                              ")
	print("              | |_) )  ____  ___   ___    / ____  | |__    _____  _ _  ____        ")
	print("              |  __/  / _  |/ __  / __    \___  \ |  __)  /  _  \| '_|/ __ \       ")
	print("              | |    / (_| |\__ \ \__ \    ___  / | |___ (  (_)  ) | |  ___/       ")
	print("              |_|    \_____| ___/  ___/   |____/  |_____) \_____/|_|  \____        ")
function()

def create_new_user(username, password):
    """
    Function to create a new user with a username and password
    """
    new_user = User(username, password)
    return new_user

def save_user(user):
    """
    Function to save a new user
    """
    user.save_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def login_user(username, password):
    """
    function that checks whether a user exist and then login the user in
    """
    check_user = Credentials.verify_user(username, password)
    return check_user

def create_new_credential(account, userName, password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account, userName, password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials.save_details()

def display_accounts_details():
    """
    Function that returns all the saved credential
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)

def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)
