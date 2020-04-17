def register():
    result_uname = user_name()
    while result_uname is None:
        result_uname = user_name()
    else:
        pass
    result_pswd = pass_word()
    while result_pswd is None:
        result_pswd = pass_word()
    else:
        pass
    result_prof = profession()
    while result_prof is None:
        result_prof = profession()
    print("Registration Successful")
    return result_uname, result_pswd, result_prof


def log_in():
    pass


def log_out():
    pass


def doctor():
    pass


def patient():
    pass


def receptionist():
    pass


def user_name():
    uname = input("Enter Username:")
    dict = {"smallalphabets": 0, "numbers": 0, "capitalalphabets": 0, "othercharacters": 0}
    for x in uname:
        if x.islower():
            dict["smallalphabets"] += 1
        elif x.isdigit():
            dict["numbers"] += 1
        elif x.isupper():
            dict["capitalalphabets"] += 1
        else:
            dict["othercharacters"] += 1
    if dict["smallalphabets"] == 0 or dict["capitalalphabets"] > 0 or \
            dict["othercharacters"] > 0 or len(uname) < 8 or len(uname) > 15:
        print("Username Doesn't match the criteria",
              "\nAccepts only small alphabets and numbers",
              "\nLength should be greater than 8 and less than 15")
    else:
        return uname



def pass_word():
    pswd = input("Enter Password:")
    dict_pswd = {"Smallalphabets": 0, "numbers": 0, "capitalalphabets": 0, "specialcharacters": 0, "othercharacters": 0}
    for x in pswd:
        if x.islower():
            dict_pswd["Smallalphabets"] += 1
        elif x.isdigit():
            dict_pswd["numbers"] += 1
        elif x.isupper():
            dict_pswd["capitalalphabets"] += 1
        elif x == "$" or x == "#" or x == "@":
            dict_pswd["specialcharacters"] += 1
        else:
            dict_pswd["othercharacters"] += 1
    if dict_pswd["Smallalphabets"] == 0 or dict_pswd["numbers"] == 0 or dict_pswd["capitalalphabets"] == 0 or dict_pswd[
        "specialcharacters"] == 0 or dict_pswd["othercharacters"] > 0 or len(pswd) < 6 or len(pswd) > 12:
        print("PasswordDoesn't match the criteria",
              "\nPlease follow the below guidelines",
              "\n1. At least 1 letter between [a-z]",
              "\n2. At least 1 number between [0-9]",
              "\n3. At least 1 letter between [A-Z]",
              "\n4. At least 1 character from [$#@]",
              "\n5. Minimum length of transaction Password : 6",
              "\n6. Maximum length of transaction Password : 12")
    else:
        return pswd


def profession():
    prof = input("Enter profession: Doctor(D), Receptionist(R), Patient(P):")
    if prof == "D" or prof == "R" or prof == "P":
        return prof
    else:
        print("Incorrect profession Entered")
        return None

def main():
    dict_users = {}
    uname, pswd, prof = register()
    tuple_pswd = (pswd, prof)
    dict_users[uname] = tuple_pswd
    print(dict_users.items())


if __name__ == "__main__":
    main()
