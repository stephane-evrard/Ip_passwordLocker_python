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
