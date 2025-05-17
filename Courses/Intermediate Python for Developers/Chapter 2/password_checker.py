password = "not_very_secure_2023"


def password_checker(submission):
    if password == submission:
        print("Successful login!")
    else:
        print("Incorrect password")


password_checker(password)
